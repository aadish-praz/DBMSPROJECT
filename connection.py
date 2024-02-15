
from typing import Generator
from sqlalchemy import text
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session


CONNECTION_STRING='mysql+mysqlconnector://root:Aadish12345@127.0.0.1'

engine = create_engine(
    url=CONNECTION_STRING,
    echo=True
)

def get_db():
    with engine.connect() as connection:
        res = connection.execute(text('show tables;'))
        print(res)
        
if __name__ == "__main__":
    get_db()