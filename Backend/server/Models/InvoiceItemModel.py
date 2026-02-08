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
        
    # @hybrid_property
    # def total_price(self) -> float:
    #     return (self.price - self.discount) * self.quantity
    
    # @total_price.inplace.expression
    # @classmethod
    # def _total_price_expression(cls) -> ColumnElement[float]:
    #     return type_coerce(((cls.price - cls.discount) * cls.quantity), Float)
    
    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="invoice_items")
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    service: Mapped["Service"] = relationship("Service", back_populates="invoice_items")
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
