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
