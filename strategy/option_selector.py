def get_atm_strike(price, step=50):
    """Round to nearest strike"""
    return round(price / step) * step


def option_symbol(signal, spot):

    atm = get_atm_strike(spot)

    if signal == "BUY_CE":
        return f"{atm} CE", atm, "CE"

    if signal == "BUY_PE":
        return f"{atm} PE", atm, "PE"

    return None, None, None