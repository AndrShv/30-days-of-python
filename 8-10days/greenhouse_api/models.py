from pydantic import BaseModel


class GreenHouse(BaseModel):
    sensor_id: str
    temperature: float
    humidity: float
    critical_humidity: float = 30.0
    status: str = "active"
    critical_temperature: float = 30.0

    def needs_water(self) -> bool:
        if self.humidity < self.critical_humidity:
            print("Need to water")
            return True
        else:
            print("It is unnecessary to water")
            return False


    def need_to_fix(self) -> bool:
        if self.temperature > self.critical_temperature:
            print("Need to fix")
            self.status = "inactive"
            return True
        else:
            print("It is unnecessary to fix")
            return False


class FixRequest(BaseModel):
    sensor_id: str

