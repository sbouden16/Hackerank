from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.sql import select
import pymysql
from sqlalchemy.orm import sessionmaker

#ask about sequence() id = Column(Integer, Sequence('user_seq'), primary_key=True)

url = db.engine.url.URL(
    drivername="mysql+pymysql",
    username="root",
    password="123456",
    host="localhost",
    database="test_pipenv",
    )

engine = db.create_engine(url,echo = True)
conn = engine.connect()
#metadata = db.MetaData()


'''users = db.Table('users', metadata,
              db.Column('id', db.Integer, primary_key=True),
              db.Column('name', db.String(16),index = True),
                 db.Column('fullname', db.String(16), index=True),
              )
'''
#metadata.create_all(engine)

#users = db.Table('users', metadata, autoload=True, autoload_with=engine)
#Session = sessionmaker(bind=engine)
#session = Session()
#c1 = db.insert(users,id=1, "name"='Station Road Nanded',
#               "fullname"='ravi@gmail.com')

#session.add(c1)
#session.commit()
#s = select([users])
#result = conn.execute(s)
#for i in result:
    #print(i)
#print(conn)


Base = declarative_base()
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  fullname = Column(String(150))
  #password = Column(String(50))

  def __init__(self, name, fullname):#, password):
    self.name = name
    self.fullname = fullname
    #self.password = password


#Base.metadata.create_all(engine, checkfirst=True)
#Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User('ed', 'Ed Jones')
session.add(ed_user)
session.commit()
'''
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)
'''


#metadata = db.MetaData()


'''users = db.Table('users', metadata,
              db.Column('id', db.Integer, primary_key=True),
              db.Column('name', db.String(16),index = True),
                 db.Column('fullname', db.String(16), index=True),
              )
'''
#metadata.create_all(engine)

#users = db.Table('users', metadata, autoload=True, autoload_with=engine)
#Session = sessionmaker(bind=engine)
#session = Session()
#c1 = db.insert(users,id=1, "name"='Station Road Nanded',
#               "fullname"='ravi@gmail.com')

#session.add(c1)
#session.commit()
#s = select([users])
#result = conn.execute(s)
#for i in result:
#print(i)
#print(conn)

'''
Base = declarative_base()


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  fullname = Column(String(150))
  #password = Column(String(50))

  def __init__(self, name, fullname):  # , password):
    self.name = name
    self.fullname = fullname
    #self.password = password


#Base.metadata.create_all(engine, checkfirst=True)
#Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User('ed', 'Ed Jones')
session.add(ed_user)
session.commit()
'''




'''
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)
'''
