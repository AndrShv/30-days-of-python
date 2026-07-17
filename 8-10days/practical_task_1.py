class TemperatureSensor:
    def __init__(self, sensor_id: str, raw_value: float):
        self.sensor_id = sensor_id
        self.raw_value = raw_value
        self.critical_temp = 30.0

    def convert_to_fahrenheit(self) -> float:
        return (self.raw_value * 1.8) + 32

    def return_sensor_info(self) -> str:
        return f"Sensor ID: {self.sensor_id}, Temperature: {self.raw_value}°C, Critical Temp: {self.critical_temp}°C"

    def __str__(self) -> str:
        return f"Sensor ID: {self.sensor_id}, Temperature: {self.raw_value}°C, Critical Temp: {self.critical_temp}°C"


temperatures = [
    TemperatureSensor("T001", 25.0),
    TemperatureSensor("T002", 35.5),
    TemperatureSensor("T003", 15.2),
]

non_accessible_sensors = []
available_sensors = []


def is_critical(sensor_list: list) -> list:
    for temp_sensor in sensor_list:
        if temp_sensor.raw_value > temp_sensor.critical_temp:
            non_accessible_sensors.append(
                (temp_sensor.sensor_id, temp_sensor.raw_value)
            )
    return non_accessible_sensors


low_temp_sensors = is_critical(temperatures)
print("Датчики с критической температурой:", low_temp_sensors)


def get_available_sensors(sensor_list: list) -> list:
    for temp_sensor in sensor_list:
        if temp_sensor.raw_value <= temp_sensor.critical_temp:
            available_sensors.append((temp_sensor.sensor_id, temp_sensor.raw_value))
    return available_sensors


available_sensors = get_available_sensors(temperatures)
print("Доступные датчики:", available_sensors)


for temp_sensor in temperatures:
    print(temp_sensor)
