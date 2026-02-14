import os
from dotenv import load_dotenv

load_dotenv()

UPSTOX_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")
UPSTOX_API_KEY = os.getenv("UPSTOX_API_KEY")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")