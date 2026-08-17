class GreenhouseModel:
    sensor_id: str
    humidity: float

    def __init__(self, sensor_id: str, humidity: float):
        self.sensor_id = sensor_id
        self.humidity = humidity


    def __eq__(self, other):
        if not isinstance(other, GreenhouseModel):
            return False
        return self.sensor_id == other.sensor_id

    def __str__(self):
        return f"[Датчик {self.sensor_id}] Влажность: {self.humidity}%"


sensor1 = GreenhouseModel("T01", 45.5)
sensor2 = GreenhouseModel("T01", 80.0)
sensor3 = GreenhouseModel("T02", 45.5)

print(sensor1)
print(sensor1 == sensor2)
print(sensor1 == sensor3)
print(sensor1 == "T01")

