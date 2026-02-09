from enum import Enum
from pydantic import BaseModel, Field, ConfigDict

class ServiceCategory(str, Enum):
    manufacturing = "manufacturing"
    spare_parts = "spare_parts"
    others = "others"

class ServiceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    category: ServiceCategory
    description: str
    service_code: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

class ServiceRead(BaseModel):
    id: int
    name: str
    category: ServiceCategory
    description: str
    price: float
    
    model_config = ConfigDict(from_attributes=True)