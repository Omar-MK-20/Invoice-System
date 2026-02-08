from pydantic import BaseModel, Field, ConfigDict
from datetime import date


class CarCreate(BaseModel):
    model_name: str = Field(min_length=1, max_length=50)
    plate_no: str = Field(min_length=1, max_length=15)
    chassis_no: str = Field(min_length=1, max_length=50)
    motor_no: str = Field(min_length=1, max_length=50)
    registration_date: date
    meter_reading: int = Field(ge=0)
    customer_id: int



class CarRead(BaseModel):
    id: int
    model_name: str
    chassis_no: str
    motor_no: str
    plate_no: str
    meter_reading: int
    registration_date: date
    
    model_config = ConfigDict(from_attributes=True)