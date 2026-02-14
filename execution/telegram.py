import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    )