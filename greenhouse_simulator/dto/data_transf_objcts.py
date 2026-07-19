from pydantic import BaseModel, Field

class SensorRequest(BaseModel):
    sensor_id: str = Field(..., min_length=3, max_length=20)
    name: str = Field(..., min_length=3, max_length=20)
    temperature: float = Field(..., gt=0)
    humidity: float = Field(..., gt=0)
    light: float = Field(..., gt=0)
    status: str = Field(..., min_length=3, max_length=20)
    created_at: str = Field(..., min_length=3, max_length=20)



class SensorResponse(SensorRequest):
    sensor_id: int
    name: str
    temperature: float
    humidity: float
    light: float
    status: str
    created_at: str
