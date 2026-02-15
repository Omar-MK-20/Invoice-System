from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.DB.connection import Base, engine

from server.Routers.customer import customerRouter
from server.Routers.service import serviceRouter
from server.Routers.car import carRouter
from server.Routers.invoice import invoiceRouter

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://invoice-system-frontend-two.vercel.app",
    "https://invoice-system-frontend-two.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(customerRouter)
app.include_router(serviceRouter)
app.include_router(carRouter)
app.include_router(invoiceRouter)



@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return {"Invoice System": "Hello from invoice system"}
