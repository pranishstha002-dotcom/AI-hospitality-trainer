# AI-hospitality-trainer
HSS lets hospitality learners practice realistic guest-service interactions with an AI guest, receive structured assessment, and build a track record.
# Front Desk Trainer — Flask edition

Hospitality skills simulator. Runs entirely on a **free local model via
Ollama** — no API key, no billing, ever. Same features as the original
Streamlit app, rebuilt as a conventional server-rendered Flask app:

- Real password-hashed accounts (bcrypt)
- An agentic "Duty Manager" coach with tool-calling (SOP lookup, hotel
  policy lookup, example phrasing)
- A live AI-guest roleplay for each scenario
- LLM-graded assessment against each scenario's SOP checklist
- A local leaderboard, badges, and difficulty gating (Easy → Medium → Hard)

## Setup (one-time)

```bash
# 1. Install Ollama
#    https://ollama.com/download

# 2. Pull a tool-calling-capable model
ollama pull llama3.1

# 3. Install Python dependencies
pip install -r requirements.txt
```

## Run

```bash
flask --app app run --debug
```

or simply:

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project layout

```
app.py            Flask routes (auth, practice flow, progress, leaderboard)
config.py         Model name, data file path, session secret key
scenarios.py      All scenario data (situations, SOPs, personas, openers)
storage.py        JSON-file "database": accounts (bcrypt) + session history
ai.py             Ollama calls: guest simulation, grading, agentic coach
logic.py          Scoring, difficulty gating, badges, leaderboard
templates/        Jinja2 HTML templates
static/style.css  Styling
hss_data.json     Created on first run — accounts + everyone's session history
```

## How the Flask version differs from the Streamlit original

- **No `st.session_state`.** Login state lives in Flask's signed session
  cookie (just a small `{name, role}` dict). The in-progress conversation
  for an *active* practice run (transcript, coach Q&A log, pending result)
  lives server-side in an in-memory dict (`ACTIVE_PRACTICE` in `app.py`),
  keyed by a random id stored in the cookie — so a long roleplay is never
  limited by cookie size the way stuffing the whole transcript into the
  session would be.
- **Server-rendered pages instead of a reactive script.** Each Streamlit
  "stage" (browse → brief → chat → results) is now its own route:
  `/practice`, `/practice/<id>/brief`, `/practice/<id>/chat`,
  `/practice/<id>/results`. Sending a chat message or asking the coach a
  question is a normal form POST that redirects back to the chat page
  (POST/redirect/GET), so refreshing never resubmits a message.
  Chat pages retain **all your data** — this is a page reload, not a live
  chat app; expect a brief pause while the model responds.
- **Everything else — scenario data, prompts, grading rubric, gating
  rules, badge rules, and the local JSON storage format — is unchanged**,
  so `hss_data.json` files are compatible in spirit (same shape), and
  anyone who understood the original scoring/badge logic will recognize
  it here verbatim in `logic.py` and `ai.py`.

## Notes

- This is designed for solo or small-classroom local use on one machine
  (one Flask process). The in-memory active-session store means an app
  restart clears any conversation *in progress*; completed, scored
  sessions are already saved to `hss_data.json` by that point and are
  never lost.
- Set `FLASK_SECRET_KEY` as an environment variable before running in any
  shared setting (it defaults to a fixed dev value otherwise).
- Swap `HSS_MODEL` (env var) to use a different Ollama model.
