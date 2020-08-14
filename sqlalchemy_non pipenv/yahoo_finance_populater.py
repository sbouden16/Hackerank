import yahoofinancials
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime,
ForeignKey,Float)

Base = declarative_base()
class yahoo_table(Base):
    __tablename__ = 'yahoo_financials'
    asset_id = Column(Integer(), primary_key=True)
    stock_name = Column(String(50), index=True)
    stock_acronim = Column(String(255))
    stock_price = Column(Float())
    def __repr__(self):
        return "yahoo_table(stock_name='{self.stock_name}', " \
            "stock_acronim='{self.stock_acronim}', " \
            "stock_price='{self.stock_price}', " \
            "quantity={self.quantity}, ".format(self=self)