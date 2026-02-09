from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.DB.connection import get_db
from server.Schemas.CustomerSchema import CustomerCreate
from server.Services.CustomerService import createCustomer, getCustomers

customerRouter = APIRouter(prefix="/customers", tags=["Customer"])


@customerRouter.post("", status_code=status.HTTP_201_CREATED)
def create_customer(bodyDate: CustomerCreate, db: Session = Depends(get_db)):
    return createCustomer(bodyDate, db=db)


@customerRouter.get("", status_code=status.HTTP_200_OK)
def get_customers(db: Session = Depends(get_db)):
    return getCustomers(db)

