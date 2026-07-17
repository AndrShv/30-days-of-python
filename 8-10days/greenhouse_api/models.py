from pydantic import BaseModel


class GreenHouse(BaseModel):
    sensor_id: str
    temperature: float
    humidity: float

    def __init__(
        self,
        sensor_id: str,
        temperature: float,
        humidity: float,
        critical_humidity: float,
    ):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity
        self.critical_humidity = 30.0

    def needs_water(humidity: float, self) -> bool:
        if humidity < self.critical_humidity:
            print("Need to water")
            return True
        else:
            print("It is unnecessary to water")
            return False
