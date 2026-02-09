from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from server.Models.CarModel import Car
from server.Models.CustomerModel import Customer
from server.Schemas.CarSchema import CarCreate


def createCar(car: CarCreate, db: Session):
    
    existCustomer = db.scalar(select(Customer).where(Customer.id == car.customer_id))
    if(not existCustomer):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "customer not found"})
    
    
    getChassisNoStmt = select(Car).where(Car.chassis_no == car.chassis_no)
    existChassisNo = db.scalar(statement=getChassisNoStmt)
    if(existChassisNo):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "chassis number already exist"})

    getMotorNoStmt = select(Car).where(Car.motor_no == car.motor_no)
    existMotorNo = db.scalar(statement=getMotorNoStmt)
    if(existMotorNo):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "motor number already exist"})
    
    getPlateNoStmt = select(Car).where(Car.plate_no == car.plate_no)
    existPlateNo = db.scalar(statement=getPlateNoStmt)
    if(existPlateNo):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "plate number already exist"})

    newCar = Car(**car.model_dump())
    db.add(newCar)
    db.commit()
    db.refresh(newCar)
    return {"message": "car created successfully", "result": newCar}