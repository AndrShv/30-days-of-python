import random
from abc import ABC, abstractmethod
from typing import Union, Any
from greenhouse_simulator.utils.log_funcs import log_method


class Sensor(ABC):
    __sensor_id: str
    __name: str

    def __init__(self, sensor_id: str, name: str):
        self.sensor_id = sensor_id
        self.name = name

    @abstractmethod
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "name": self.name,
            "sensor_type": "default"
        }


class TemperatureSensor(Sensor):
    temperature = round(random.uniform(15.0, 35.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "name": self.name,
            "temperature": self.temperature,
            "sensor_type": "temperature"
        }


class HumiditySensor(Sensor):
    humidity = round(random.uniform(20.0, 80.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "name": self.name,
            "humidity": self.humidity,
            "sensor_type": "humidity"
        }


class LightSensor(Sensor):
    light = round(random.uniform(20.0, 80.0), 1)

    @log_method
    def get_sensor_info(self) -> dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "name": self.name,
            "light": self.light,
            "sensor_type": "humidity"
        }
