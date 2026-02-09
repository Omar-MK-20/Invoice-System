from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from server.Models.CustomerModel import Customer
from server.Models.CarModel import Car
from server.Schemas.CustomerSchema import CustomerCreate

def createCustomer(customer: CustomerCreate, db: Session):
    getEmailStmt = select(Customer).where(Customer.email == customer.email)
    existEmail = db.scalar(statement=getEmailStmt)
    if(existEmail):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "email already exist"})

    getPhoneStmt = select(Customer).where(Customer.phone == customer.phone)
    existPhone = db.scalar(statement=getPhoneStmt)
    if(existPhone):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "phone number already exist"})

    newCustomer = Customer(**customer.model_dump())
    db.add(newCustomer)
    db.commit()
    db.refresh(newCustomer)
    return {"message": "customer created successfully", "result": newCustomer}


def getCustomers(db: Session):
    getCustomersStmt = select(Customer, Car).join(Customer.cars).options(selectinload(Customer.cars)).order_by(Customer.id)

    customers = db.scalars(getCustomersStmt).all()

    if (customers.__len__() == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "no customers found"})

    return {"message": "success", "customers": customers}

