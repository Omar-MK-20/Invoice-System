from fastapi import APIRouter, Depends, status
from fastapi import status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from server.Schemas.InvoiceSchema import InvoiceCreate
from server.Services.InvoiceService import createInvoice, getInvoices, getSingleInvoice
from server.DB.connection import get_db




invoiceRouter = APIRouter(prefix="/invoices", tags=["Invoice"])


@invoiceRouter.post("", status_code=status.HTTP_201_CREATED)
def create_invoice(bodyData: InvoiceCreate, db: Session = Depends(get_db)):
    return createInvoice(bodyData, db)


@invoiceRouter.get("", status_code=status.HTTP_200_OK)
def get_invoices(customerName:Optional[str] = None, invoiceNo: Optional[str] = None, dateFrom: Optional[date] = None, dateTo: Optional[date] = None ,db: Session = Depends(get_db)):
    return getInvoices(customerName, invoiceNo, dateFrom, dateTo, db)


@invoiceRouter.get("/{id}", status_code=status.HTTP_200_OK)
def get_single_invoices(id: int, db: Session = Depends(get_db)):
    return getSingleInvoice(id, db)


