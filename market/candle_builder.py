import pandas as pd
from datetime import datetime

class CandleBuilder:

    def __init__(self):
        self.current_minute = None
        self.ohlc = None

    def update(self, ltp):

        now = datetime.now().replace(second=0, microsecond=0)

        if self.current_minute != now:
            finished = self.ohlc
            self.current_minute = now
            self.ohlc = {"open": ltp, "high": ltp, "low": ltp, "close": ltp}
            return finished

        self.ohlc["high"] = max(self.ohlc["high"], ltp)
        self.ohlc["low"] = min(self.ohlc["low"], ltp)
        self.ohlc["close"] = ltp
        return None