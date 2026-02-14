from data_ingestion.option_chain import get_option_chain


def compute_pcr_around_atm(spot):

    data = get_option_chain("NIFTY")
    if not data:
        return None, None

    strikes = sorted(data.keys(), key=lambda x: abs(float(x)-spot))[:5]

    ce_oi = 0
    pe_oi = 0
    ce_change = 0
    pe_change = 0

    for strike in strikes:
        row = data[strike]

        ce = row.get("CE", {})
        pe = row.get("PE", {})

        ce_oi += ce.get("openInterest", 0)
        pe_oi += pe.get("openInterest", 0)

        ce_change += ce.get("changeinOpenInterest", 0)
        pe_change += pe.get("changeinOpenInterest", 0)

    if ce_oi == 0:
        pcr = 0
    else:
        pcr = round(pe_oi / ce_oi, 2)

    oi_change = round(((pe_change - ce_change) / max(ce_oi+pe_oi,1))*100,2)

    return pcr, oi_change