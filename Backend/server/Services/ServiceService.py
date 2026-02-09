from fastapi import status, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from server.Models.ServiceModel import Service
from server.Schemas.ServiceSchema import ServiceCreate

def createService(service: ServiceCreate, db: Session):
    getNameStmt = select(Service).where(Service.name == service.name)
    existName = db.scalar(getNameStmt)
    if(existName):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "name already exists"})
    
    getServiceCodeStmt = select(Service).where(Service.service_code == service.service_code)
    existServiceCode = db.scalar(getServiceCodeStmt)
    if(existServiceCode):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "service code already exists"})
    
    newService = Service(**service.model_dump())

    db.add(newService)
    db.commit()
    db.refresh(newService)

    return {"message": "service created successfully", "result": newService}


def getServices(db: Session):
    getServicesStmt = select(Service)

    services = db.scalars(getServicesStmt).all()

    if(not services):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error":"no services found"})
    
    return {"message": "success", "services": services}
