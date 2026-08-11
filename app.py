"""
Front Desk Trainer — Hospitality Skills Simulator (Flask / Ollama edition)

Runs entirely on a FREE local model via Ollama — no API key, no billing, ever.
Includes: real password-hashed accounts (bcrypt), an agentic "Duty Manager"
coach with tool-calling, a local leaderboard, badges, and difficulty gating.

Setup (one-time):
    1. Install Ollama: https://ollama.com/download
    2. Pull a tool-calling-capable model:   ollama pull llama3.1
    3. pip install -r requirements.txt

Run:
    flask --app app run --debug
    (or:  python app.py)
"""

import random
import time
import uuid
from datetime import datetime

from flask import Flask, redirect, render_template, request, session, url_for, flash

from ai import HOTEL_POLICIES, call_agent_coach, call_grading, call_guest
from config import SECRET_KEY
from confirmation import build_confirmation
from logic import compute_badges, get_leaderboard, lock_reason, overall_score, scenario_unlocked
from scenarios import (
    DEPARTMENT_ICON,
    DEPARTMENT_ORDER,
    DIFFICULTY_COLOR,
    SCENARIOS,
    SCENARIOS_BY_ID,
)
from storage import add_user_session, create_account, get_user_sessions, slugify, verify_login

# Guest emotional intensity is now a randomly assigned trait rather than
# something the trainee picks — real front-desk staff don't know a guest's
# mood in advance. Weighted so "medium" is the common case.
_EMOTION_WEIGHTS = {"low": 25, "medium": 50, "high": 25}


def random_emotion() -> str:
    return random.choices(list(_EMOTION_WEIGHTS), weights=list(_EMOTION_WEIGHTS.values()), k=1)[0]

app = Flask(__name__)
app.secret_key = SECRET_KEY

# --------------------------------------------------------------------------
# In-memory store for ACTIVE practice sessions (mid-conversation state).
#
# The Flask session cookie only ever holds a small login dict plus a random
# "pid" pointing in here — never the full transcript — so conversations of
# any length are never limited by cookie size. This is a single-process,
# in-memory store: fine for solo/local use or a small class on one machine;
# an app restart clears any interaction in progress (completed results are
# already persisted to hss_data.json by then, so nothing scored is lost).
# --------------------------------------------------------------------------
ACTIVE_PRACTICE = {}


def current_practice():
    pid = session.get("pid")
    if not pid:
        return None
    return ACTIVE_PRACTICE.get(pid)


def start_practice(scenario_id: str, opener: str, emotion: str = "medium"):
    pid = uuid.uuid4().hex
    session["pid"] = pid
    ACTIVE_PRACTICE[pid] = {
        "scenario_id": scenario_id,
        "transcript": [{"role": "assistant", "content": opener}],
        "coach_log": [],
        "result": None,
        "new_badges": [],
        "emotion": emotion if emotion in ("low", "medium", "high") else "medium",
    }
    return ACTIVE_PRACTICE[pid]


def clear_practice():
    pid = session.pop("pid", None)
    if pid:
        ACTIVE_PRACTICE.pop(pid, None)


# --------------------------------------------------------------------------
# Auth helpers
# --------------------------------------------------------------------------


def login_required(view):
    def wrapped(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    wrapped.__name__ = view.__name__
    return wrapped


@app.context_processor
def inject_user():
    return {"current_user": session.get("user")}


@app.template_filter("friendly_date")
def friendly_date(iso_string):
    try:
        return datetime.fromisoformat(iso_string).strftime("%d %b %Y, %H:%M")
    except (ValueError, TypeError):
        return iso_string


# --------------------------------------------------------------------------
# Login / signup / logout
# --------------------------------------------------------------------------


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user"):
        return redirect(url_for("practice_browse"))

    if request.method == "POST":
        name = request.form.get("name", "")
        password = request.form.get("password", "")
        if not name.strip() or not password:
            flash("Enter your name and password.", "error")
        else:
            ok, err, account = verify_login(name, password)
            if ok:
                session["user"] = account
                return redirect(url_for("practice_browse"))
            flash(err, "error")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if session.get("user"):
        return redirect(url_for("practice_browse"))

    if request.method == "POST":
        name = request.form.get("name", "")
        password = request.form.get("password", "")
        password2 = request.form.get("password2", "")
        role = request.form.get("role", "student")

        if not name.strip() or not password:
            flash("Enter a name and password.", "error")
        elif len(password) < 4:
            flash("Password must be at least 4 characters.", "error")
        elif password != password2:
            flash("Passwords don't match.", "error")
        else:
            ok, err = create_account(name, password, role)
            if ok:
                session["user"] = {"name": name.strip(), "role": role}
                return redirect(url_for("practice_browse"))
            flash(err, "error")

    return render_template("signup.html")


@app.route("/logout")
def logout():
    clear_practice()
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/")
def index():
    return redirect(url_for("practice_browse")) if session.get("user") else redirect(url_for("login"))


# --------------------------------------------------------------------------
# Practice: browse
# --------------------------------------------------------------------------


@app.route("/practice")
@login_required
def practice_browse():
    clear_practice()
    user = session["user"]
    user_slug = slugify(user["name"])
    sessions_for_gating = get_user_sessions(user_slug)

    departments = []
    for dept in DEPARTMENT_ORDER:
        dept_scenarios = [s for s in SCENARIOS if s["department"] == dept]
        if not dept_scenarios:
            continue
        rows = []
        for s in dept_scenarios:
            unlocked = scenario_unlocked(s, sessions_for_gating, user["role"])
            rows.append(
                {
                    "scenario": s,
                    "unlocked": unlocked,
                    "lock_reason": lock_reason(s) if not unlocked else "",
                }
            )
        departments.append({"name": dept, "icon": DEPARTMENT_ICON.get(dept, "🏨"), "rows": rows})

    return render_template(
        "browse.html",
        departments=departments,
        difficulty_color=DIFFICULTY_COLOR,
    )


# --------------------------------------------------------------------------
# Practice: brief -> start -> chat -> finish -> results
# --------------------------------------------------------------------------


@app.route("/practice/<scenario_id>/brief")
@login_required
def practice_brief(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    if not scenario:
        return redirect(url_for("practice_browse"))

    user = session["user"]
    sessions_for_gating = get_user_sessions(slugify(user["name"]))
    if not scenario_unlocked(scenario, sessions_for_gating, user["role"]):
        flash("That scenario is still locked.", "error")
        return redirect(url_for("practice_browse"))

    return render_template(
        "brief.html",
        scenario=scenario,
        difficulty_color=DIFFICULTY_COLOR,
        policies=HOTEL_POLICIES,
        confirmation=build_confirmation(scenario),
    )


@app.route("/practice/<scenario_id>/start", methods=["POST"])
@login_required
def practice_start(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    if not scenario:
        return redirect(url_for("practice_browse"))
    start_practice(scenario_id, scenario["opener"], random_emotion())
    return redirect(url_for("practice_chat", scenario_id=scenario_id))


@app.route("/practice/<scenario_id>/chat")
@login_required
def practice_chat(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    state = current_practice()
    if not scenario or not state or state["scenario_id"] != scenario_id:
        return redirect(url_for("practice_brief", scenario_id=scenario_id))

    student_turns = sum(1 for t in state["transcript"] if t["role"] == "user")
    return render_template(
        "chat.html",
        scenario=scenario,
        transcript=state["transcript"],
        coach_log=state["coach_log"],
        student_turns=student_turns,
        emotion=state.get("emotion", "medium"),
        ended=state.get("ended", False),
        policies=HOTEL_POLICIES,
        confirmation=build_confirmation(scenario),
    )


@app.route("/practice/<scenario_id>/send", methods=["POST"])
@login_required
def practice_send(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    state = current_practice()
    if not scenario or not state or state["scenario_id"] != scenario_id:
        return redirect(url_for("practice_brief", scenario_id=scenario_id))

    if state.get("ended"):
        flash("The guest has already left this conversation — end the interaction to see your assessment.", "error")
        return redirect(url_for("practice_chat", scenario_id=scenario_id))

    message = request.form.get("message", "").strip()
    if message:
        state["transcript"].append({"role": "user", "content": message})
        try:
            reply, ended = call_guest(scenario, state["transcript"], state.get("emotion", "medium"))
            state["transcript"].append({"role": "assistant", "content": reply})
            state["ended"] = ended
        except Exception as e:
            flash(f"The guest simulation hit a snag: {e}", "error")

    return redirect(url_for("practice_chat", scenario_id=scenario_id))


@app.route("/practice/<scenario_id>/coach", methods=["POST"])
@login_required
def practice_coach(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    state = current_practice()
    if not scenario or not state or state["scenario_id"] != scenario_id:
        return redirect(url_for("practice_brief", scenario_id=scenario_id))

    question = request.form.get("question", "").strip()
    if question:
        answer = call_agent_coach(scenario, state["transcript"], question)
        state["coach_log"].append({"q": question, "a": answer})

    return redirect(url_for("practice_chat", scenario_id=scenario_id))


@app.route("/practice/<scenario_id>/finish", methods=["POST"])
@login_required
def practice_finish(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    state = current_practice()
    if not scenario or not state or state["scenario_id"] != scenario_id:
        return redirect(url_for("practice_brief", scenario_id=scenario_id))

    student_turns = sum(1 for t in state["transcript"] if t["role"] == "user")
    if student_turns < 2 and not state.get("ended"):
        flash("Send at least two responses before ending the interaction.", "error")
        return redirect(url_for("practice_chat", scenario_id=scenario_id))

    user = session["user"]
    user_slug = slugify(user["name"])

    try:
        result = call_grading(scenario, state["transcript"])
    except Exception as e:
        flash(f"Couldn't generate the assessment just now: {e}", "error")
        return redirect(url_for("practice_chat", scenario_id=scenario_id))

    sessions_before = get_user_sessions(user_slug)
    badges_before = compute_badges(sessions_before)

    entry = {
        "id": str(int(time.time() * 1000)),
        "scenario_id": scenario["id"],
        "title": scenario["title"],
        "department": scenario["department"],
        "difficulty": scenario["difficulty"],
        "date": datetime.now().isoformat(),
        "scores": result,
    }
    add_user_session(user_slug, user["name"], entry)

    sessions_after = get_user_sessions(user_slug)
    badges_after = compute_badges(sessions_after)
    new_badges = [b for b in badges_after if b["label"] not in {x["label"] for x in badges_before}]

    state["result"] = result
    state["new_badges"] = new_badges

    return redirect(url_for("practice_results", scenario_id=scenario_id))


@app.route("/practice/<scenario_id>/results")
@login_required
def practice_results(scenario_id):
    scenario = SCENARIOS_BY_ID.get(scenario_id)
    state = current_practice()
    if not scenario or not state or state["scenario_id"] != scenario_id or not state["result"]:
        return redirect(url_for("practice_browse"))

    result = state["result"]
    return render_template(
        "results.html",
        scenario=scenario,
        result=result,
        overall=overall_score(result),
        new_badges=state["new_badges"],
    )


# --------------------------------------------------------------------------
# Progress + Leaderboard
# --------------------------------------------------------------------------


@app.route("/progress")
@login_required
def progress():
    user = session["user"]
    user_slug = slugify(user["name"])
    sessions = get_user_sessions(user_slug)

    stats = None
    badges = []
    if sessions:
        overalls = [overall_score(s["scores"]) for s in sessions]
        sop_scores = [s["scores"]["sopCompliance"] for s in sessions]
        stats = {
            "count": len(sessions),
            "avg_overall": round(sum(overalls) / len(overalls)),
            "avg_sop": round(sum(sop_scores) / len(sop_scores)),
        }
        badges = compute_badges(sessions)

    return render_template(
        "progress.html",
        sessions=sessions,
        stats=stats,
        badges=badges,
        overall_score=overall_score,
    )


@app.route("/leaderboard")
@login_required
def leaderboard():
    user = session["user"]
    user_slug = slugify(user["name"])
    entries = get_leaderboard()
    return render_template("leaderboard.html", entries=entries, user_slug=user_slug)


if __name__ == "__main__":
    app.run(debug=True)
