from broker.stream import UpstoxStreamer
from market.candle_builder import CandleBuilder
from indicators.ta_engine import TAEngine
from strategy.rule_engine import generate_signal
from execution.telegram import send
from data_ingestion.tick_decoder import extract_ltp

import pandas as pd

candles = []
builder = CandleBuilder()
ta = TAEngine()

def on_tick(raw):

    ltp = extract_ltp(raw)   # we'll implement decoder next
    candle = builder.update(ltp)

    if candle:
        candles.append(candle)
        df = pd.DataFrame(candles)

        df = ta.compute(df)
        signal = generate_signal(df)

        if signal:
            send(f"NIFTY SIGNAL: {signal}")

UpstoxStreamer(on_tick).start()