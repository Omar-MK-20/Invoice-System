from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from Schemas.ServiceSchema import ServiceRead


class InvoiceItemCreate(BaseModel):
    service_id: int
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    discount: float = Field(default=0, ge=0)


class InvoiceItemRead(BaseModel):
    id: int
    service: ServiceRead
    quantity: int
    price: float
    discount: float
    total_price: float
    
    model_config = ConfigDict(from_attributes=True)


class InvoiceCreate(BaseModel):
    reception_engineer: str = Field(default="Omar Mohamed", min_length=1, max_length=50)
    invoice_no: str = Field(min_length=1, max_length=100)
    invoice_date: date
    customer_id: int
    car_id: int
    invoice_items: list[InvoiceItemCreate]


class InvoiceRead(BaseModel):
    id: int
    invoice_no: str
    invoice_date: date
    total_amount: float
    customer_id: int
    car_id: int
    invoice_items: list[InvoiceItemRead]
    
    model_config = ConfigDict(from_attributes=True)




