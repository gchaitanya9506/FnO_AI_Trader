from datetime import datetime, timedelta
from strategy.signal_analyzer import market_sentiment, confidence_score


def format_signal(signal):

    sentiment = market_sentiment(signal["pcr"])
    confidence = confidence_score(
        signal["rsi"],
        signal["macd_cross"],
        signal["oi_change"],
        signal["pcr"]
    )

    bars = "█" * (confidence // 10) + "░" * (10 - confidence // 10)

    urgency = "HIGH ⚡" if confidence > 80 else "MEDIUM"

    now = datetime.now()
    valid_till = (now + timedelta(minutes=15)).strftime("%H:%M")

    msg = f"""
🚨 LIVE SIGNAL

🚀 BUY {signal['option']} @ ₹{signal['entry']}
📊 PCR: {signal['pcr']} 📈 {sentiment} | RSI: {signal['rsi']} | OI Change: ↗️{signal['oi_change']}%
🎯 Target: ₹{signal['target']} | SL: ₹{signal['sl']}
🔥 Confidence: {confidence}% {bars} | Spot: ₹{signal['spot']} | {signal['reason']}
⏰ Generated: {now.strftime("%H:%M:%S")} | Valid till: {valid_till} | Urgency: {urgency}
"""

    return msg