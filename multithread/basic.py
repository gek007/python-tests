import asyncio


async def worker(id: int) -> None:
    print(f"Worker {id} started")
    await asyncio.sleep(1)
    print(f"Worker {id} finished")


async def main() -> None:
    tasks = [worker(i) for i in range(10)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
