import os
from pathlib import Path
from typing import Annotated, TypedDict

import gradio as gr
import requests
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

_pkg_dir = Path(__file__).resolve().parent
for _env in (_pkg_dir / ".env", _pkg_dir.parent / ".env"):
    if _env.exists():
        load_dotenv(_env)
        break
else:
    raise FileNotFoundError(
        f"Environment file not found (tried {_pkg_dir / '.env'}, {_pkg_dir.parent / '.env'})"
    )


pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"

memory = MemorySaver()

serper = GoogleSerperAPIWrapper()
tool_search = Tool(
    name="search",
    func=serper.run,
    description="Useful for when you need more information from an online search",
)


def push(text: str):
    """Send a push notification to the user"""
    requests.post(
        pushover_url,
        data={"token": pushover_token, "user": pushover_user, "message": text},
    )


tool_push = Tool(
    name="send_push_notification",
    func=push,
    description="useful for when you want to send a push notification",
)

tools = [tool_search, tool_push]


class State(TypedDict):
    messages: Annotated[list, add_messages]
    age: int


graph_builder = StateGraph(State)

# Step 3
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    print(state)
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

# Step 4
graph_builder.add_conditional_edges("chatbot", tools_condition, "tools")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Step 5
graph = graph_builder.compile(checkpointer=memory)
try:
    from IPython import get_ipython
    from IPython.display import Image, display

    if get_ipython() is not None:
        display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    pass


config = {"configurable": {"thread_id": "1"}}


def chat(user_input: str, history):
    result = graph.invoke(
        {"messages": [{"role": "user", "content": user_input}]}, config=config
    )
    return result["messages"][-1].content


if __name__ == "__main__":
    gr.ChatInterface(chat).launch()
    print("Done")
