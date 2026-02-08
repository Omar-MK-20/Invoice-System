from pydantic import BaseModel, EmailStr, Field, ConfigDict

class CustomerCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(pattern=r"^(?:\+20|0020|0)1[0125]\d{8}$")


class CustomerRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    
    model_config = ConfigDict(from_attributes=True)
