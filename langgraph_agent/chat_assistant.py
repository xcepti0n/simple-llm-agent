
from typing import Annotated, Literal, TypedDict
from typing import List
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables.config import RunnableConfig

# local library
from langgraph_agent.tools import get_current_time

class State(TypedDict):
    """
    State for the AI Agent.
    add_messages function auto add message history to the list.
    """
    messages: Annotated[List, add_messages]

# Use the model which you are running in ollama
MODEL="ollama:qwen3:4b"

# Useful for storing memory, checkpoint for each session.
config: RunnableConfig = {
    'configurable': { 'thread_id': 'main'}
}
# One of the ways to store memory, otherways include postgres db etc.
# It helps to keep the context in the conversation.
# Message history helps, but it is more efficient.
memory = InMemorySaver()

agent = create_react_agent(
    model=MODEL,
    tools=[get_current_time], # add multiple tools here
    prompt=(
        "You are AI Agent, you are personal assistant of the user with access to all the tools"
        "Use tools as necessary to fulfil user requirements."
    ),
    checkpointer=memory
)

def langgraph_chat_assistant():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        state: State = {"messages": [HumanMessage(content=user_input)]}
        response = agent.invoke(state, config=config)
        print_cyan(f"AI Agent: {response['messages'][-1].content}")

def print_cyan(message):
    """
    Explanation:
    \033[ — Start of ANSI escape sequence
    96m — Bright cyan text
    \033[0m — Reset formatting
    """
    print(f"\033[96m{message}\033[0m")

if __name__ == "__main__":
    langgraph_chat_assistant()
