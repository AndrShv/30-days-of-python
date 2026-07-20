from typing import Any, Generator, Dict, AsyncGenerator, Optional



async def sensor_data_stream(sensors: list, count: Optional[int] = None) -> AsyncGenerator[dict[str, Any], None]:
    if count is None or count <= 0:
        count = len(sensors)
    critical_sensors = await check_temperature(sensors)
    iteration = 0
    while iteration < count:
        for sensor in critical_sensors:
            sensors_info = {
                "id": sensor.id,
                "name": sensor.name,
                "temperature": sensor.temperature,
                "humidity": sensor.humidity,
                "light": sensor.light,
                "critical_humidity": sensor.critical_humidity,
                "critical_temperature": sensor.critical_temperature,
                "status": sensor.status,
            }
            yield sensors_info
        iteration += 1


class CriticalGreenhouseException(Exception):
    pass


async def check_temperature(sensors: list) -> list:
    critical_sensors = []
    if len(sensors) == 0:
        return critical_sensors
    for sensor in sensors:
        try:
            if sensor.temperature > 30:
                critical_sensors.append(sensor)
                raise CriticalGreenhouseException(f"Критический перегрев! {sensor.temperature}°C")
        except CriticalGreenhouseException as ex:
            print(f"[WARNING] {ex} + id: {sensor.id}")
    return critical_sensors


