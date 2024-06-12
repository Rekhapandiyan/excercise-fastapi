from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from .config import settings


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Password24@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#try:
#    conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='Password24')
#    cursor = conn.cursor()
#    print("Database connection was successful")
    
#except Exception as error:
#    print("Connecting to database failed")
#    print("Error: ", error)