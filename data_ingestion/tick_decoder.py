from data_ingestion.proto import market_data_pb2


def extract_ltp(message: bytes):
    """
    Decode Upstox protobuf message and extract LTP
    Returns dict: {instrument_key: ltp}
    """
    feed = market_data_pb2.FeedResponse()
    feed.ParseFromString(message)

    prices = {}

    for key, value in feed.feeds.items():

        # full feed
        if value.HasField("ff"):
            ltp = value.ff.marketFF.ltpc.ltp
            prices[key] = ltp

        # ltpc only feed
        elif value.HasField("ltpc"):
            ltp = value.ltpc.ltp
            prices[key] = ltp

    return prices