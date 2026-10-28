import asyncio
import httpx

async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        # await переключает управление в Event Loop, пока ждем ответ
        response = await client.get(url)
        return response.json()

async def main():
    # Запуск задач параллельно (аналог CompletableFuture.allOf в Java)
    results = await asyncio.gather(
        fetch_data("https://api.example.com/v1"),
        fetch_data("https://api.example.com/v2"),
    )
    print(results)

# Точка входа
asyncio.run(main())