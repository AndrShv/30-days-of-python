import asyncio
import datetime
from typing import Any, Generator, Dict, AsyncGenerator
import time


async def sensor_data_stream(sensors: list, count: int) -> AsyncGenerator[dict[str, Any], None]:
    if count is None or count <= 0:
        count = len(sensors)
    await check_temperature(list(sensors))
    iteration = 0
    while iteration < count:
        for sensor in sensors:
            sensors_info = {
                "sensor_id": sensor.sensor_id,
                "name": sensor.name,
                "temperature": sensor.temperature,
                "humidity": sensor.humidity,
                "light": sensor.light,
            }
            yield sensors_info
        iteration += 1


class CriticalGreenhouseException(Exception):
    pass


async def check_temperature(sensors: list):
    if len(sensors) == 0:
        return
    for sensor in sensors:
        try:
            if sensor.temperature > 30:
                raise CriticalGreenhouseException(f"Критический перегрев! {sensor.temperature}°C")
        except CriticalGreenhouseException as ex:
            print(f"[WARNING] {ex} + sensor_id: {sensor.sensor_id}")


async def simulate_greenhouse(sensors: list, count: int = 5):
    if len(list) == 0:
        return
    date = time.strftime("%d.%m.%Y", time.localtime())
    gen = sensor_data_stream(sensors, count=count)
    async for sensor_data in gen:
        await asyncio.sleep(2)
        with open("greenhouse_simulator/logs/greenhouse_log.txt", "w") as log_file:
            context = {
                "timestamp": datetime.datetime.now().isoformat(),
                "data": date
            }
            log_file.write(str(context))
            log_file.write("\n")
