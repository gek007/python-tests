import asyncio
import time


def sync_func(test_param: str) -> str:
    time.sleep(1)
    return f"Sync function result: {test_param}"


async def async_func(test_param: str) -> str:
    await asyncio.sleep(1)
    return f"Async function result: {test_param}"


async def my_func() -> None:
    await asyncio.sleep(1)
    print("My function is r unning")


async def main():

    result = await asyncio.create_task(my_func())
    print(result)

    start_time = time.time()
    sync_result = sync_func("Hello")
    async_result = await async_func("Hello")
    end_time = time.time()
    print(f"Sync function took {end_time - start_time} seconds")
    print(f"Async function took {end_time - start_time} seconds")
    print(sync_result)
    print(async_result)


if __name__ == "__main__":
    asyncio.run(main())
