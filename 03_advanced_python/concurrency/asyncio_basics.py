import asyncio

async def fetch_sensor_data()-> int:
    print("Запрос отправлен...")
    sum = 2+2
    await asyncio.sleep(2)
    print("Данные пришли!")
    print(sum)

async def main():
    await asyncio.gather(fetch_sensor_data(), fetch_sensor_data(), fetch_sensor_data())

asyncio.run(main())