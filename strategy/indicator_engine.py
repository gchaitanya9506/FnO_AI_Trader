import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from database.db import SessionLocal
from database.models import Candle


def load_recent_candles(instrument, limit=200):

    db = SessionLocal()

    rows = (
        db.query(Candle)
        .filter(Candle.instrument == instrument)
        .order_by(Candle.time.desc())
        .limit(limit)
        .all()
    )

    db.close()

    if not rows:
        return None

    data = [
        {
            "time": r.time,
            "open": r.open,
            "high": r.high,
            "low": r.low,
            "close": r.close
        }
        for r in reversed(rows)
    ]

    return pd.DataFrame(data)


def compute_indicators(df):

    df["rsi"] = RSIIndicator(df["close"], window=14).rsi()

    macd = MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    return df