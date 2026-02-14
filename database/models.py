from sqlalchemy import Column, Integer, Float, String, DateTime
from database.db import Base

class Candle(Base):
    __tablename__ = "candles"

    id = Column(Integer, primary_key=True, index=True)
    instrument = Column(String)
    time = Column(DateTime)

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)