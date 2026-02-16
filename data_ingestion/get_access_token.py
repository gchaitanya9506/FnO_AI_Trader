import requests
import webbrowser
import urllib.parse
import os
from dotenv import load_dotenv, set_key

load_dotenv()

API_KEY = os.getenv("UPSTOX_API_KEY")
API_SECRET = os.getenv("UPSTOX_API_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Step 1: Generate login URL
auth_url = f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={API_KEY}&redirect_uri={REDIRECT_URI}"

print("\nOpen this URL and login:\n")
print(auth_url)

webbrowser.open(auth_url)

# Step 2: Get code from redirect
auth_code = input("\nPaste the code from browser URL: ").strip()

# Step 3: Exchange code for token
url = "https://api.upstox.com/v2/login/authorization/token"

data = {
    "code": auth_code,
    "client_id": API_KEY,
    "client_secret": API_SECRET,
    "redirect_uri": REDIRECT_URI,
    "grant_type": "authorization_code"
}

headers = {"Accept": "application/json"}

response = requests.post(url, data=data, headers=headers)
token_data = response.json()

if "access_token" not in token_data:
    print("\nERROR:", token_data)
    exit()

access_token = token_data["access_token"]

# Step 4: Save to .env automatically
set_key(".env", "UPSTOX_ACCESS_TOKEN", access_token)

print("\n✅ Access token saved successfully!")
print("You can now run the trading bot.")