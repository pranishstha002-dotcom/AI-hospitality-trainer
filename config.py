"""
Config — Front Desk Trainer (Flask edition)
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Any Ollama model that supports tool calling; swap freely.
MODEL = os.environ.get("HSS_MODEL", "llama3.1")

DATA_FILE = BASE_DIR / "hss_data.json"

# Used to sign the Flask session cookie (which only ever holds a small login
# dict + a random practice-session id — never the full transcript). Override
# with a real secret via the FLASK_SECRET_KEY env var in any shared/deployed
# setting; the fallback below is fine for solo local use.
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me-1f8a2c")
