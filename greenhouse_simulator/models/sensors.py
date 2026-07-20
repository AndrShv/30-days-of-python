import random
from abc import ABC, abstractmethod
from typing import Union, Any
from greenhouse_simulator.utils.log_funcs import log_method


class Sensor(ABC):
    __id: int
    __name: str

    def __init__(self, id: int, name: str):
        self.id = id or random.randint(1000, 9999)
        self.name = name

    @abstractmethod
    def get_sensor_info(self) -> dict[str, Any]:
        pass


class TemperatureSensor(Sensor):
    temperature = round(random.uniform(15.0, 35.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "temperature": round(random.uniform(15.0, 35.0), 1),
            "humidity": 0.0,
            "light": 0.0,
            "status": "active"
        }


class HumiditySensor(Sensor):
    humidity = round(random.uniform(20.0, 80.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "temperature": 0.0,
            "humidity": round(random.uniform(20.0, 80.0), 1),
            "light": 0.0,
            "status": "active"
        }


class LightSensor(Sensor):
    light = round(random.uniform(20.0, 80.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "temperature": 0.0,
            "humidity": 0.0,
            "light": round(random.uniform(100.0, 900.0), 1),
            "status": "active"
        }
