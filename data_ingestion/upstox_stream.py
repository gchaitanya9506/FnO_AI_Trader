import os
import json
import ssl
import websocket
import requests
from dotenv import load_dotenv
from database.save_candle import insert_candle
from data_ingestion.tick_decoder import extract_ltp
from data_ingestion.candle_builder import CandleBuilder
from strategy.signal_engine import generate_signal
from execution.telegram import send_telegram
from execution.message_formatter import format_signal

load_dotenv()

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

builder = CandleBuilder()


# STEP 1 — Get Authorized Websocket URL
def get_feed_url():
    url = "https://api.upstox.com/v3/feed/market-data-feed/authorize"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    if data.get("status") != "success":
        raise Exception(f"Auth failed: {data}")

    return data["data"]["authorized_redirect_uri"]


# STEP 2 — When socket connects
def on_open(ws):
    print("🟢 Connected to Upstox live feed")

    # subscribe NIFTY index
    subscribe = {
        "guid": "test",
        "method": "sub",
        "data": {
            "mode": "full",
            "instrumentKeys": ["NSE_INDEX|Nifty 50"]
        }
    }

    ws.send(json.dumps(subscribe))


# STEP 3 — Receive ticks
def on_message(ws, message):
    prices = extract_ltp(message)

    for instrument, ltp in prices.items():
        candle = builder.update(instrument, ltp)

        print("LIVE:", instrument, ltp)

        if candle:
            candle["instrument"] = instrument
            insert_candle(candle)
            signal = generate_signal(instrument)
            if signal:
                msg = format_signal(signal)
                print(msg)
                send_telegram(msg)


# STEP 4 — Errors
def on_error(ws, error):
    print("🔴 Error:", error)


# STEP 5 — Close
def on_close(ws, close_status_code, close_msg):
    print("🔴 Connection closed")


# STEP 6 — Start stream
def start_stream():
    socket_url = get_feed_url()
    print("Connecting to:", socket_url)

    ws = websocket.WebSocketApp(
        socket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    print("Starting Upstox Stream...")
    start_stream()