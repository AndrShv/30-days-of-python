import asyncio


async def async_worker(future: asyncio.Future):
    await asyncio.sleep(2)
    future.set_result("Данные из будущего!")


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(async_worker(fut))

    print("Ждем, пока кто-то заполнит Future...")
    result = await fut
    print(f"Ура, Future заполнен: {result}")


asyncio.run(main())