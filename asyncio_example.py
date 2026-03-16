import asyncio


async def main():
    print("Start of main routine")
    await asyncio.sleep(1)
    print("End of main routine")


asyncio.run(main())
