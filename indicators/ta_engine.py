import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD

class TAEngine:

    def compute(self, df):
        df["rsi"] = RSIIndicator(df["close"], 14).rsi()
        macd = MACD(df["close"])
        df["macd"] = macd.macd()
        df["signal"] = macd.macd_signal()
        return df