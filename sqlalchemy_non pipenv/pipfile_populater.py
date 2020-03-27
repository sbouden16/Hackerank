from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from yahoofinancials import YahooFinancials
from decimal import *
from Mysql_connector import sql_connector as sq_c
import sqlalchemy as db
from yahoo_finance_populater import yahoo_table


metadata = db.MetaData()
Base = yahoo_table()
Base.metadata.create_all(sq_c().engine)




Session = sessionmaker(bind=sq_c().engine)
session = Session()

stock_apple = yahoo_table(
    stock_name='Apple',
    stock_acronim='APPL',
    stock_price= 45,

    )

session.add(stock_apple)
session.commit()

"""
users = db.Table('yahoo_financials', metadata,
              Column('id', db.Integer, primary_key=True),
              Column('stock_name', db.String(16),nullable=False),
              Column('stock_acronim', db.String(16),nullable=False),
              Column('stock_price', db.DECIMAL, nullable=False)
              )


"""

#metadata.create_all(sq_c().engine)

#metadata.create_all(sq_c().engine)



#name = "ryanair"

#ins = users.insert().values(stock_name = name, stock_acronim = "ARYY", stock_price = 34)
#sq_c().execute(ins)
#print(YahooFinancials(values[name]).get_current_price())


#dele = users.delete().where("id" =="12")
#result = conn.execute(dele)




#Session = sessionmaker(bind=engine)
#session = Session()
#c1 = users("id" == 1, "name" == "sergio", "fullname" == "cortes")

#session.add(c1)

#session.commit()
#s = select([users])
#result = conn.execute(s)
#for i in result:
#print(i)

