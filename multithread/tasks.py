import asyncio


async def worker(id: int) -> None:
    print(f"Worker {id} started")
    await asyncio.sleep(1)
    print(f"Worker {id} finished")


async def main() -> None:

    task1 = asyncio.create_task(worker(1))
    task2 = asyncio.create_task(worker(2))
    task3 = asyncio.create_task(worker(3))

    await asyncio.gather(task1, task2, task3)


if __name__ == "__main__":
    asyncio.run(main())
