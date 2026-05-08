import asyncio

import aiofiles


async def _async_stream_gen(file_path: str):
    async with aiofiles.open(file_path, mode="r") as file:
        async for line in file:
            yield line


async def main():
    async for line in _async_stream_gen("README.md"):
        print(line)


if __name__ == "__main__":
    asyncio.run(main())
