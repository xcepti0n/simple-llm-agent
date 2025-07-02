import asyncio
import datetime

from typing import Any

from strands import Agent, tool
from strands.models.ollama import OllamaModel
from strands_tools import calculator

@tool
def get_current_time() -> dict:
    '''
    This tool gets the current local time using system commands.
    '''
    now = datetime.datetime.now()
    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S")}

# I am just using it so that I can control the colours it prints in cole.
class CustomPrintingCallbackHandler:
    """Handler for streaming text output and tool invocations to stdout."""

    def __init__(self) -> None:
        """Initialize handler."""
        self.tool_count = 0
        self.previous_tool_use = None

    def __call__(self, **kwargs: Any) -> None:
        """Stream text output and tool invocations to stdout.

        Args:
            **kwargs: Callback event data including:
                - reasoningText (Optional[str]): Reasoning text to print if provided.
                - data (str): Text content to stream.
                - complete (bool): Whether this is the final chunk of a response.
                - current_tool_use (dict): Information about the current tool being used.
        """
        reasoningText = kwargs.get("reasoningText", False)
        data = kwargs.get("data", "")
        complete = kwargs.get("complete", False)
        current_tool_use = kwargs.get("current_tool_use", {})

        if reasoningText:
            print(reasoningText, end="")

        if data:
            print_ai_response(data, end="" if not complete else "\n")

        if current_tool_use and current_tool_use.get("name"):
            tool_name = current_tool_use.get("name", "Unknown tool")
            if self.previous_tool_use != current_tool_use:
                self.previous_tool_use = current_tool_use
                self.tool_count += 1
                print_tool(f"\nTool #{self.tool_count}: {tool_name}")

        if complete and data:
            print("\n")

# async def process_streaming_response(agent, message):
#     agent.stream_async(message)
    # async for event in agent_stream:
    #     print(event["contentBlockDelta"]["delta"]["text"])

def strands_chat_assistant():
    # Create an Ollama model instance
    ollama_model = OllamaModel(
        host="http://localhost:11434",  # Ollama server address
        model_id="qwen2.5:3b"             # Specify which model to use
    )

    # Create an agent using the Ollama model and an existing calcular tool and custom tool to get time.
    # If you do not pass callback_handler it used default CustomPrintingCallbackHandler which print same as
    # our custom one, but without colours
    agent = Agent(model=ollama_model, tools=[get_current_time, calculator], callback_handler=CustomPrintingCallbackHandler())

    while True:
        print("\n")
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        # Simpler option
        message = agent(user_input).message.get("content")[-1].get("text")
        
        # await process_streaming_response(agent, user_input)

def print_ai_response(message, end=None):
    print_custom("96", message, end)

def print_tool(message, end=None):
    print_custom("33", message, end)

def print_custom(color_code: str, message:str, end):
    """
    Explanation:
    \033[ — Start of ANSI escape sequence
    color_code: 96 —  cyan text
    color_code: 33 —  yellow text
    \033[0m — Reset formatting
    """
    print(f"\033[{color_code}m{message}\033[0m", end=end)

if __name__ == "__main__":
    # For simple usage without streaming
    strands_chat_assistant()

    # With Streaming
    # asyncio.run(strands_chat_assistant())