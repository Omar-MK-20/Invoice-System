from server.DB.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, ForeignKey
from typing import TYPE_CHECKING
from datetime import date

if (TYPE_CHECKING):
    from CustomerModel import Customer
    from InvoiceModel import Invoice

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    model_name: Mapped[str] = mapped_column(String(50), nullable=False)
    chassis_no: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    motor_no: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    plate_no: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    registration_date: Mapped[date] = mapped_column(Date, default=lambda: date.today() , nullable=False)
    meter_reading: Mapped[int] = mapped_column(Integer, nullable=False)
    
    invoices: Mapped[list["Invoice"]] = relationship("Invoice", back_populates="car")

    customer: Mapped["Customer"] = relationship("Customer",back_populates="cars")
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)