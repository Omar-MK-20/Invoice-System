from pydantic import BaseModel, Field
from datetime import date
from Schemas.CustomerSchema import CustomerSchema


class InvoiceItemSchema(BaseModel):
    service_id: int
    quantity: int = Field(ge=0)
    price: float = Field(gt=0)
    discount: float = Field(default=0, ge=0)

class InvoiceSchema(BaseModel):
    reception_engineer: str = Field(default="Omar Mohamed")
    invoice_no: str
    invoice_date: date
    customer_id: int
    car_id: int
    invoice_items: list[InvoiceItemSchema]


class InvoiceResponse(BaseModel):
    id: int
    invoice_no: str
    total_amount: float


class InvoiceItemResponse(BaseModel):
    id: int
    reception_engineer: str
    invoice_no: str
    invoice_date: date
    total_amount: float
    customer: CustomerSchema
    # car: CarSchema









