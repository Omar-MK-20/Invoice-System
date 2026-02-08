from pydantic import BaseModel

class CustomerSchema(BaseModel):
    name: str
    email: str
    phone: str

    # cars: list[CarSchema] | CarSchema


