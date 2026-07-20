import os
import json
import tempfile
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

# ----------------------------
# Google Credentials
# ----------------------------

GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")

if GOOGLE_CREDENTIALS_JSON:
    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    )

    temp.write(GOOGLE_CREDENTIALS_JSON.encode())

    temp.close()

    GOOGLE_CREDENTIALS = temp.name

else:
    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")

# ----------------------------
# Validation
# ----------------------------

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found")

if not SPREADSHEET_ID:
    raise ValueError("SPREADSHEET_ID not found")

if not GOOGLE_CREDENTIALS:
    raise ValueError("Google credentials not found")