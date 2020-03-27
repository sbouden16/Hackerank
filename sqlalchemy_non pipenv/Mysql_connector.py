import sqlalchemy as db
import pymysql

def sql_connector():
    url = db.engine.url.URL(

        drivername="mysql+pymysql",
        username="root",
        password="123456",
        host="localhost",
        database="test_pipenv",

        )

    engine = db.create_engine(url, echo=True)
    metadata = db.MetaData()
    conn = engine.connect()
    return conn