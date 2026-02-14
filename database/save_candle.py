from database.db import SessionLocal
from database.models import Candle

def insert_candle(data):

    db = SessionLocal()

    candle = Candle(
        instrument=data["instrument"],
        time=data["time"],
        open=data["open"],
        high=data["high"],
        low=data["low"],
        close=data["close"],
    )

    db.add(candle)
    db.commit()
    db.close()