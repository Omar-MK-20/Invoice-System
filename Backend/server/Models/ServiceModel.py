from server.DB.connection import Base
from sqlalchemy import String, Numeric, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from typing import TYPE_CHECKING

class Category(enum.Enum):
    manufacturing = "manufacturing"
    spare_parts = "spare_parts"
    others = "others"


if TYPE_CHECKING:
    from InvoiceItemModel import InvoiceItem

class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category: Mapped[Category] = mapped_column(Enum(Category), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    service_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)

    invoice_items: Mapped[list["InvoiceItem"]] = relationship("InvoiceItem", back_populates="service")