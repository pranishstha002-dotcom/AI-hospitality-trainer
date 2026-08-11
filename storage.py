"""
Local "database" — a JSON file, keyed by a slug of the account name.
Real bcrypt password hashing runs server-side, so the hash and salt never
leave this machine.
"""

import json
import re
from datetime import datetime

import bcrypt

from config import DATA_FILE


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "guest"


def load_data() -> dict:
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            data = {}
    else:
        data = {}
    data.setdefault("accounts", {})
    data.setdefault("users", {})
    return data


def save_data(data: dict) -> None:
    DATA_FILE.write_text(json.dumps(data, indent=2))


def get_user_sessions(slug: str) -> list:
    data = load_data()
    return data.get("users", {}).get(slug, {}).get("sessions", [])


def add_user_session(slug: str, display_name: str, entry: dict) -> None:
    data = load_data()
    data["users"].setdefault(slug, {"name": display_name, "sessions": []})
    data["users"][slug]["sessions"].insert(0, entry)
    save_data(data)


def create_account(name: str, password: str, role: str) -> tuple:
    slug = slugify(name)
    data = load_data()
    if slug in data["accounts"]:
        return False, "That name is already registered — log in instead."
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    data["accounts"][slug] = {
        "name": name,
        "role": role,
        "password_hash": password_hash,
        "created_at": datetime.now().isoformat(),
    }
    save_data(data)
    return True, None


def verify_login(name: str, password: str) -> tuple:
    slug = slugify(name)
    data = load_data()
    account = data["accounts"].get(slug)
    if not account:
        return False, "No account with that name yet — sign up first.", None
    if not bcrypt.checkpw(password.encode("utf-8"), account["password_hash"].encode("utf-8")):
        return False, "Incorrect password.", None
    return True, None, {"name": account["name"], "role": account["role"]}
