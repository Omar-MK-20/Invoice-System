from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from server.Schemas.ServiceSchema import ServiceCreate
from server.DB.connection import get_db
from server.Services.ServiceService import createService, getServices

serviceRouter = APIRouter(prefix="/services", tags=["Service"])

@serviceRouter.post("", status_code=status.HTTP_201_CREATED)
def create_service(bodyData: ServiceCreate, db: Session = Depends(get_db)):
    return createService(bodyData, db)


@serviceRouter.get("", status_code=status.HTTP_200_OK)
def get_services(db: Session = Depends(get_db)):
    return getServices(db)