import asyncio

from agents.mcp import MCPServerStdio

fetch_stdio = {"command": "uvx", "args": ["mcp-server-fetch"]}


async def main():
    async with MCPServerStdio(
        params=fetch_stdio, client_session_timeout_seconds=60
    ) as server:
        fetch_tools = await server.list_tools()
        print(fetch_tools)


asyncio.run(main())
