from fastapi import APIRouter, Depends
from server.Schemas.CustomerSchema import CustomerCreate
from server.DB.connection import get_db
from server.Models.CustomerModel import Customer
from sqlalchemy.orm import Session

customerRouter = APIRouter(prefix="/customers", tags=["Customer"])


@customerRouter.post("", status_code=201)
def createCustomer(customer: CustomerCreate, db: Session = Depends(get_db)):
    newCustomer = Customer(**customer.model_dump())
    db.add(newCustomer)
    db.commit()
    db.refresh(newCustomer)
    return newCustomer