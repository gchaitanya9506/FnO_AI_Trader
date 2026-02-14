import websocket
import json
import requests
import certifi
from config.settings import UPSTOX_TOKEN, UPSTOX_API_KEY

class UpstoxStreamer:

    def __init__(self, on_tick):
        self.on_tick = on_tick

    def _get_feed_url(self):
        url = "https://api.upstox.com/v3/feed/market-data-feed/authorize"
        headers = {
            "Authorization": f"Bearer {UPSTOX_TOKEN}",
            "x-api-key": UPSTOX_API_KEY
        }
        return requests.get(url, headers=headers).json()["data"]["authorized_redirect_uri"]

    def start(self):
        ws = websocket.WebSocketApp(
            self._get_feed_url(),
            on_message=self._on_message
        )
        ws.run_forever(sslopt={"ca_certs": certifi.where()})

    def _on_message(self, ws, message):
        self.on_tick(message)