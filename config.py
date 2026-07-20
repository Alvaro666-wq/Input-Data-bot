import json
import tempfile
import os

GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")

temp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")

temp.write(GOOGLE_CREDENTIALS_JSON.encode())

temp.close()

GOOGLE_CREDENTIALS = temp.name

BOT_TOKEN = os.getenv("BOT_TOKEN")

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")