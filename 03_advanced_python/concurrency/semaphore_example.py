from asyncio import Semaphore, gather, run, sleep


async def fetch_page(semaphore: Semaphore, url_id: int):
    async with semaphore:
        print(f"Начали скачивать страницу {url_id}")
        await sleep(1)
        print(f"Закончили страницу {url_id}")


async def main():
    semaphore = Semaphore(2)
    tasks = [fetch_page(semaphore, i) for i in range(1, 6)]
    await gather(*tasks)


if __name__ == "__main__":
    run(main())