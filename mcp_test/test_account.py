import asyncio
import sys
from pathlib import Path

from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio

PROJECT_ROOT = Path(__file__).resolve().parent.parent

params = {
    "command": sys.executable,
    "args": [str(PROJECT_ROOT / "mcp_test" / "account.py")],
    "cwd": str(PROJECT_ROOT),
}


# async def main():
#     async with MCPServerStdio(
#         params=params, client_session_timeout_seconds=60
#     ) as server:
#         tools = await server.list_tools()
#         for tool in tools:
#             print(f"{tool.name}: {tool.description}")

instructions = "You are able to manage an account for a client, and answer questions about the account."
request = "1. put 100$ on the account 2. withdraw 20$ from the account \
           4. put 50$ on the account \
           5. withdraw 10$ from the account \
           6. put 20$ on the account \
           7. withdraw 30$ from the account \
           8. put 40$ on the account \
           9. withdraw 50$ from the account \
           10. put 60$ on the account \
           11. withdraw 70$ from the account \
           12. get the balance of the account and print all the steps you made icluding the balance after each step"
model = "gpt-4.1-mini"


async def main():
    async with MCPServerStdio(
        params=params, client_session_timeout_seconds=30
    ) as mcp_server:
        agent = Agent(
            name="account_manager",
            instructions=instructions,
            model=model,
            mcp_servers=[mcp_server],
        )
        with trace("account_manager"):
            result = await Runner.run(agent, request)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
