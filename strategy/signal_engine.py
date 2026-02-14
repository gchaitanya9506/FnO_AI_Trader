from strategy.indicator_engine import load_recent_candles, compute_indicators
from strategy.option_selector import option_symbol
from strategy.risk_manager import calculate_trade_levels
from strategy.oi_metrics import compute_pcr_around_atm


def generate_signal(instrument="NSE_INDEX|26000"):

    df = load_recent_candles(instrument)

    if df is None or len(df) < 50:
        return None

    df = compute_indicators(df)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    spot = last["close"]

    pcr, oi_change = compute_pcr_around_atm(spot)
    if pcr is None:
        return None

    signal = None

    if prev["macd"] < prev["macd_signal"] and last["macd"] > last["macd_signal"] and last["rsi"] > 55:
        signal = "BUY_CE"

    elif prev["macd"] > prev["macd_signal"] and last["macd"] < last["macd_signal"] and last["rsi"] < 45:
        signal = "BUY_PE"

    if not signal:
        return None

    option, strike, option_type = option_symbol(signal, spot)

    # temporary premium estimate (we will replace with real option LTP later)
    premium_estimate = round(spot * 0.005, 2) 
    
    entry, sl, t1, t2 = calculate_trade_levels(premium_estimate)

    signal_data = {
    "signal": signal,          # BUY_CE / BUY_PE
    "strike": strike,          # numeric ATM strike
    "option": option,          # "25900 CE"
    "option_type": option_type,
    "entry": entry,
    "target": t1,
    "sl": sl,
    "spot": spot,
    "rsi": round(last["rsi"],1),
    "macd_cross": True,
    "oi_change": oi_change,
    "pcr": pcr,
    "reason": "Strong bullish breakout + PCR support"
    }

    return signal_data