from server.DB.connection import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if (TYPE_CHECKING):
    from CarModel import Car
    from InvoiceModel import Invoice

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    phone: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)

    cars: Mapped[list["Car"]] = relationship("Car", back_populates="customer")
    invoices: Mapped[list["Invoice"]] = relationship("Invoice", back_populates="customer")




