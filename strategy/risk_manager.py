def calculate_trade_levels(premium):

    entry = premium

    sl = round(entry * 0.80, 2)        # 20% SL
    t1 = round(entry * 1.25, 2)        # 25% target
    t2 = round(entry * 1.50, 2)        # 50% target

    return entry, sl, t1, t2