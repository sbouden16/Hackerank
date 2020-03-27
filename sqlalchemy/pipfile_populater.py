from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.sql import select
import pymysql
from sqlalchemy.orm import sessionmaker


url = db.engine.url.URL(
    drivername="mysql+pymysql",
    username="root",
    password="123456",
    host="localhost",
    database="test_pipenv",
)

engine = db.create_engine(url, echo=True)
conn = engine.connect()
metadata = db.MetaData()

users = db.Table('users', metadata,
              Column('id', db.Integer, primary_key=True),
              Column('name', db.String(16),index = True),
                Column('fullname', db.String(16), index=True),
              )



metadata.create_all(engine)

ins = users.insert().values(name = "Sergio", fullname = "Cortes Satizabal")
result = conn.execute(ins)

dele = users.delete().where("id" =="12")
result = conn.execute(dele)




#Session = sessionmaker(bind=engine)
#session = Session()
#c1 = users("id" == 1, "name" == "sergio", "fullname" == "cortes")

#session.add(c1)

#session.commit()
#s = select([users])
#result = conn.execute(s)
#for i in result:
#print(i)
