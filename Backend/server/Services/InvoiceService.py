from fastapi import status
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload, joinedload
from typing import Optional
from datetime import date

from server.Models.InvoiceModel import Invoice
from server.Models.InvoiceItemModel import InvoiceItem
from server.Models.CustomerModel import Customer
from server.Models.CarModel import Car
from server.Models.ServiceModel import Service
from server.Schemas.InvoiceSchema import InvoiceCreate


def createInvoice(invoice: InvoiceCreate , db: Session):
    getCustomer = db.scalar(select(Customer).where(Customer.name == invoice.customer_name))
    if(not getCustomer):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "customer not found"})
    
    customerId = getCustomer.id
    
    existCar = db.scalar(select(Car).where(Car.id == invoice.car_id))
    if(not existCar):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "car mot found"})
    
    existInvoiceNo = db.scalar(select(Invoice).where(Invoice.invoice_no == invoice.invoice_no))
    if(existInvoiceNo):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "invoice number already exists"})
    
    if(not invoice.invoice_items):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail={"error": "you must add invoice item "})
    
    
    newInvoice = Invoice(
        reception_engineer = invoice.reception_engineer,
        invoice_no = invoice.invoice_no,
        invoice_date = invoice.invoice_date,
        customer_id = customerId,
        car_id = invoice.car_id
    )    
    
    totalAmount = 0
    
    for item in invoice.invoice_items:
        
        existService = db.scalar(select(Service).where(Service.id == item.service_id))
        if(not existService):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": f"service not found for item with service_id = {item.service_id}"})
        
        totalItem = (float(existService.price) - item.discount) * item.quantity
        totalAmount += totalItem
        
        newInvoiceItem = InvoiceItem(
            quantity = item.quantity,
            price = existService.price,
            discount = item.discount,
            total_price = totalItem,
            service_id = item.service_id
        )
        
        newInvoice.invoice_items.append(newInvoiceItem)
    
    newInvoice.total_amount = totalAmount
    
    db.add(newInvoice)
    db.commit()
    db.refresh(newInvoice)
    
    return {"message": "invoice created successfully", "result": newInvoice}


def getInvoices(customerName: Optional[int], invoiceNo: Optional[str], dateFrom: Optional[date], dateTo: Optional[date], db: Session):
    getInvoicesStmt = select(Invoice).options(joinedload(Invoice.customer), joinedload(Invoice.car)).order_by(Invoice.id)
    
    if(customerName):
        getInvoicesStmt = getInvoicesStmt.join(Invoice.customer).where(Customer.name.ilike(f"%{customerName}%"))
    
    if(invoiceNo):
        getInvoicesStmt = getInvoicesStmt.where(Invoice.invoice_no.ilike(f"%{invoiceNo}%"))
    
    if(dateFrom):
        getInvoicesStmt = getInvoicesStmt.where(Invoice.invoice_date >= dateFrom)
    
    if(dateTo):
        getInvoicesStmt = getInvoicesStmt.where(Invoice.invoice_date <= dateTo)
    
    invoices = db.scalars(getInvoicesStmt).all()
    
    if(not invoices):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "no invoices found"})
    
    return {"message": "success", "invoices": invoices}


def getSingleInvoice(invoiceId: int, db: Session):
    getInvoiceStmt = select(Invoice, Customer, Car).options(selectinload(Invoice.invoice_items).joinedload(InvoiceItem.service), joinedload(Invoice.customer), joinedload(Invoice.car)).where(Invoice.id == invoiceId)
    
    invoice = db.scalar(getInvoiceStmt)
    
    if(not invoice):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "invoice not found"})
    
    return {"message": "success", "invoice": invoice}
