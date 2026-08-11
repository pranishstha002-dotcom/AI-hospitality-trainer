"""
Scoring, difficulty gating, badges, and the leaderboard — pure functions over
the JSON-backed session data.
"""

from scenarios import DEPARTMENTS
from storage import load_data


def overall_score(scores: dict) -> int:
    keys = ["communication", "professionalism", "problemSolving", "sopCompliance", "guestSatisfaction"]
    return round(sum(scores[k] for k in keys) / len(keys))


def scenario_unlocked(scenario: dict, sessions: list, role: str) -> bool:
    if role == "instructor":
        return True
    if scenario["difficulty"] == "Easy":
        return True
    if scenario["difficulty"] == "Medium":
        return any(s["difficulty"] == "Easy" for s in sessions)
    if scenario["difficulty"] == "Hard":
        return any(s["difficulty"] == "Medium" and overall_score(s["scores"]) >= 60 for s in sessions)
    return True


def lock_reason(scenario: dict) -> str:
    if scenario["difficulty"] == "Medium":
        return "Complete an Easy scenario first"
    if scenario["difficulty"] == "Hard":
        return "Score 60+ on a Medium scenario first"
    return ""


def compute_badges(sessions: list) -> list:
    badges = []
    if any(s["scores"]["sopCompliance"] >= 90 for s in sessions):
        badges.append({"label": "SOP Star", "icon": "🛡️"})
    if len(sessions) >= 3:
        avg_sat = sum(s["scores"]["guestSatisfaction"] for s in sessions) / len(sessions)
        if avg_sat >= 85:
            badges.append({"label": "Guest Whisperer", "icon": "🌟"})
    if len(sessions) >= 3:
        last_three = sessions[:3]
        if all(overall_score(s["scores"]) >= 80 for s in last_three):
            badges.append({"label": "Five-Star Streak", "icon": "🔥"})
    depts_covered = {s["department"] for s in sessions}
    if depts_covered == set(DEPARTMENTS):
        badges.append({"label": "All-Rounder", "icon": "🎖️"})
    return badges


def get_leaderboard() -> list:
    """All student accounts ranked by best overall score, built from the same
    local file everyone on this machine shares."""
    data = load_data()
    entries = []
    for slug, account in data["accounts"].items():
        if account["role"] == "instructor":
            continue
        sessions = data.get("users", {}).get(slug, {}).get("sessions", [])
        if not sessions:
            continue
        overalls = [overall_score(s["scores"]) for s in sessions]
        entries.append(
            {
                "slug": slug,
                "name": account["name"],
                "sessions_count": len(sessions),
                "best_overall": max(overalls),
                "avg_overall": round(sum(overalls) / len(overalls)),
                "badge_count": len(compute_badges(sessions)),
            }
        )
    entries.sort(key=lambda e: e["best_overall"], reverse=True)
    return entries
