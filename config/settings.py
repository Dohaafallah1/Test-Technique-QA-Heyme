import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE_URL = os.getenv("HEYME_BASE_URL", "https://heyme-ep.dev.btc-web.fr/")
EMAIL = os.getenv("HEYME_EMAIL", "")
PASSWORD = os.getenv("HEYME_PASSWORD", "")

LOGIN_PATH = "/login"
CONTRACTS_PATH = "/contract/list"
