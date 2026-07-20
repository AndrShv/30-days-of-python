from pydantic import BaseModel, Field

class SensorRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    temperature: float = Field(default=0.0, gt=0)
    humidity: float = Field(default=0.0, gt=0)
    light: float = Field(default=0.0, gt=0)
    status: str = Field(default="active", min_length=3, max_length=20)



class SensorResponse(SensorRequest):
    id: str
    name: str
    temperature: float
    humidity: float
    light: float
    status: str

class Config:
    from_attributes = True
    orm_mode = True
