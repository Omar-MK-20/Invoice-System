import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if(not DATABASE_URL):
    raise ValueError("'DATABASE_URL' are missing in environment variable '.env' file")

engine = create_engine(DATABASE_URL)

def testDBConnection() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(select(1))
            print("INFO:     DB connected successfully")
            return True
    except Exception as e:
        print("Error:     DB connection failed")
        print(e)
        return False

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    with SessionLocal() as db:
        yield db



class Base(DeclarativeBase):
    pass
