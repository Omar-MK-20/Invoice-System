from server.DB.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from InvoiceModel import Invoice
    from ServiceModel import Service


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    discount: Mapped[float] = mapped_column(Numeric(10,2), nullable=False, default=0)
    total_price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False, default=0)
    
    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="invoice_items")
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    service: Mapped["Service"] = relationship("Service", back_populates="invoice_items")
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
