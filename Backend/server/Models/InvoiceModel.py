from server.DB.connection import Base
from datetime import date, datetime
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, DateTime, Date, Numeric, ForeignKey
from zoneinfo import ZoneInfo

egypt_timezone = ZoneInfo("Africa/Cairo")
print(egypt_timezone)

if (TYPE_CHECKING):
    from InvoiceItemModel import InvoiceItem
    from CustomerModel import Customer
    from CarModel import Car

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    reception_engineer: Mapped[str] = mapped_column(String(50), nullable=False)
    invoice_no: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    invoice_date: Mapped[date] = mapped_column(Date, default=lambda: date.today())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default= lambda: datetime.now(tz=egypt_timezone))
    total_amount: Mapped[float] = mapped_column(Numeric(12,2), nullable=False, default=0)

    invoice_items: Mapped[list["InvoiceItem"]] = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")

    customer: Mapped["Customer"] = relationship("Customer", back_populates="invoices")
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    car: Mapped["Car"] = relationship("Car", back_populates="invoices")
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
