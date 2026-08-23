import logging
import asyncio
import random

async def fetch_sensor(sensor_id: str, delay: int = 1) -> tuple:
    logging.info(f"Fetching sensor data for sensor ID: {sensor_id}")
    await asyncio.sleep(delay)
    return sensor_id, random.uniform(20, 30)