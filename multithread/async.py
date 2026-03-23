import asyncio
import time


def sync_func(test_param: str) -> str:
    time.sleep(1)
    return f"Sync function result: {test_param}"


async def async_func1(test_param: str) -> str:
    await asyncio.sleep(1)
    return f"Async function result: {test_param}"


async def async_func2(test_param: str) -> None:
    await asyncio.sleep(1)
    return f"Async function result: {test_param}"


async def main():

    # result = await asyncio.create_task(async_func2())
    # print(result)

    # start_time = time.time()
    # sync_result = sync_func("Hello")
    # async_result = await async_func1("Hello")
    # end_time = time.time()
    # print(f"Sync function took {end_time - start_time} seconds")
    # print(f"Async function took {end_time - start_time} seconds")
    # print(sync_result)
    # print(async_result)
    start_time = time.time()
    task1 = asyncio.create_task(async_func1("Hello"))
    task2 = asyncio.create_task(async_func2("Kostya is a good boy"))
    result = await asyncio.gather(task1, task2)
    end_time = time.time()
    print(result)
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
