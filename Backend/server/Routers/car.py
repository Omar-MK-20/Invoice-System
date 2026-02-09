from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.DB.connection import get_db
from server.Schemas.CarSchema import CarCreate
from server.Services.CustomerService import createCustomer, getCustomers



carRouter = APIRouter(prefix="/cars", tags=["Car"])


@carRouter.post("", status_code=status.HTTP_201_CREATED)
def create_car(bodyDate: CarCreate, db: Session = Depends(get_db)):
    return bodyDate