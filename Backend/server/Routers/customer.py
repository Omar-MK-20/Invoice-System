from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.DB.connection import get_db
from server.Schemas.CustomerSchema import CustomerCreate
from server.Services.CustomerService import createCustomer, getCustomers, getOneCustomer


customerRouter = APIRouter(prefix="/customers", tags=["Customer"])


@customerRouter.post("", status_code=status.HTTP_201_CREATED)
def create_customer(bodyData: CustomerCreate, db: Session = Depends(get_db)):
    return createCustomer(bodyData, db=db)


@customerRouter.get("", status_code=status.HTTP_200_OK)
def get_customers(db: Session = Depends(get_db)):
    return getCustomers(db)


@customerRouter.get("/{id}", status_code=status.HTTP_200_OK)
def get_single_customer(id: int, db: Session = Depends(get_db)):
    return getOneCustomer(customer_id=id, db=db)