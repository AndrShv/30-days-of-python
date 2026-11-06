import asyncio


async def background_work():
    print("1. Фоновая задача началась...")
    await asyncio.sleep(2)
    print("3. Фоновая задача завершилась!")
    return "Готово"


async def main():
    task = asyncio.create_task(background_work())

    print("2. Основной код продолжает работать, пока задача крутится в фоне...")

    result = await task
    print(f"4. Получили результат: {result}")


asyncio.run(main())