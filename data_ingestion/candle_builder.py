from datetime import datetime
from collections import defaultdict

class CandleBuilder:

    def __init__(self):
        self.current_minute = None
        self.candles = defaultdict(lambda: None)

    def update(self, instrument, price):
        now = datetime.now().replace(second=0, microsecond=0)

        candle = self.candles[instrument]

        # first tick
        if candle is None:
            self.candles[instrument] = {
                "time": now,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
            self.current_minute = now
            return None

        # new minute started → close previous candle
        if now != candle["time"]:
            closed = candle.copy()

            # start new candle
            self.candles[instrument] = {
                "time": now,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }

            return closed

        # update current candle
        candle["high"] = max(candle["high"], price)
        candle["low"] = min(candle["low"], price)
        candle["close"] = price

        return None