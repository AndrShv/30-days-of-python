import asyncio
from asyncio import Semaphore, Future
import random


async def save_files(semaphore: Semaphore, file_id: int, data: str):
    async with semaphore:
        print(f"Saving file_{file_id}.txt")
        saved_files = {}
        saved_files[file_id] = data
        await asyncio.sleep(1)
    return saved_files





async def get_cached_data(future: Future, file_id: int):
    random_file_id = random.randint(1, 5)
    print(f"Requesting cached data for file_{file_id}.txt (randomly selected file_{random_file_id}.txt)")
    await asyncio.sleep(2)
    future.set_result(f"Cached data for file_{random_file_id}.txt")


async def main():
    semaphore = Semaphore(3)
    loop = asyncio.get_running_loop()
    my_future = loop.create_future()
    asyncio.create_task(get_cached_data(my_future, 4))
    tasks = [save_files(semaphore, i, f"Data for file_{i}.txt") for i in range(1, 6)]


    files_group = asyncio.gather(*tasks)

    saved_files, cached_result = await asyncio.gather(files_group, my_future)
    print(f"Received cached data: {cached_result}")
    print(f"Saved files: {saved_files}")


if __name__ == "__main__":
    asyncio.run(main())
