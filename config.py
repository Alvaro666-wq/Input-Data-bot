import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in .env")

if not SPREADSHEET_ID:
    raise ValueError("SPREADSHEET_ID not found in .env")

if not GOOGLE_CREDENTIALS:
    raise ValueError("GOOGLE_CREDENTIALS not found in .env")    