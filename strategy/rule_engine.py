def generate_signal(df):

    last = df.iloc[-1]

    if last["rsi"] < 20 and last["macd"] > last["signal"]:
        return "BUY CALL"

    if last["rsi"] > 60 and last["macd"] < last["signal"]:
        return "BUY PUT"

    return None