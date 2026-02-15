from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.DB.connection import testDBConnection, Base, engine
import server.Models
import sys

from server.Routers.customer import customerRouter
from server.Routers.service import serviceRouter
from server.Routers.car import carRouter
from server.Routers.invoice import invoiceRouter

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://invoice-system-frontend-two.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(customerRouter)
app.include_router(serviceRouter)
app.include_router(carRouter)
app.include_router(invoiceRouter)

if not testDBConnection():
    sys.exit(1)

try:
    Base.metadata.create_all(bind=engine)
    print("tables created successfully")
except Exception as e:
    print("error in creating tables")
    print(e)


@app.get("/")
def hello():
    return {"Invoice System": "Hello form invoice system"}

