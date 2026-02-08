from fastapi import FastAPI
from server.DB.connection import testDBConnection, Base, engine
import server.Models
import sys

server = FastAPI()

if not testDBConnection():
    sys.exit(1)


try:
    Base.metadata.create_all(bind=engine)
    print("tables created successfully")
except Exception as e:
    print("error in creating tables")
    print(e)


@server.get("/")
def hello():
    return {"Invoice System": "Hello form invoice system"}