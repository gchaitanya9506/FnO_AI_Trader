import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")


def get_option_chain(symbol="NIFTY"):

    url = f"https://api.upstox.com/v2/option/chain/{symbol}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    if data.get("status") != "success":
        print("Option chain error:", data)
        return None

    return data["data"]