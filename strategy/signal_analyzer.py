def market_sentiment(pcr):
    if pcr < 0.7:
        return "Bullish"
    elif pcr > 1.3:
        return "Bearish"
    return "Neutral"


def confidence_score(rsi, macd_cross, oi_change, pcr):

    score = 50

    # RSI strength
    if rsi > 60 or rsi < 40:
        score += 10

    # MACD confirmation
    if macd_cross:
        score += 15

    # OI movement
    if oi_change > 15:
        score += 10

    # PCR support
    if (pcr < 0.8 and rsi > 50) or (pcr > 1.2 and rsi < 50):
        score += 12

    return min(score, 95)