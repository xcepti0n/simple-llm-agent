This assistant is made using below python libraries.

- langgraph
    - langchain_core
    - langchain
- ollama

See code comments to undestand more, feel free to ask for any questions.

## Prerequisite

### uv 
It can be installed using `pip install uv`

use command `uv --help` to check if it is installed correctly.

### Ollama
Install ollama - 
Install ollama model with tooling support (https://ollama.com/blog/tool-support, https://ollama.com/search?c=tools)
- `ollama run qwen3:4b` pr `ollama run llama3.2`
It opens chat terminal which you can test for chatting or just close using `/bye`.

Start ollama server
- `ollama serve`

### Installing libraries
`uv add langgraph langchain_core langchain langchain-ollama`

## Running the agent
Runs the main module i.e. main.py
`uv run -m main`

or

`.\.venv\Scripts\python.exe main.py`

or if you have globally installed modules using pip, you can simply run

`python main.py` or `python langgraph_agent/chat-assistant.py`

## Example Conversation

### Langgraph Agent example
```
Hello from simple-tool-agent!
You: Hello 
AI Agent: <think>
Okay, the user said "Hello". I need to respond appropriately. Let me check the tools available. There's a function called get_current_time that returns the current local time. Since the user just greeted me, maybe I should respond with a friendly message and also provide the current time. But wait, do I need to use the tool here? The user didn't ask for the time, but maybe offering it as a helpful gesture. However, the instructions say to use tools when necessary. If the user's query doesn't explicitly require a tool, maybe I shouldn't call it. Let me think. The user's message is just a greeting. The best response is to greet them back and offer assistance. No need for the tool call here. So I'll just respond with a friendly message.
</think>

Hello! How can I assist you today?
You: Can you tell me current time?
AI Agent: <think>
Okay, the user asked for the current time, and I used the get_current_time function. The response came back as "2025-07-01 00:33:59". I need to present this time in a friendly manner. Let me check if the date and time format is correct. The date is July 1, 2025, and the time is 12:33:59 AM. Since the user didn't specify a time zone, I'll assume it's their local time. I should format the response clearly, maybe mention the date and time together. Let me make sure there are no errors in the time. Everything looks good. Now, I'll tell the user the current time in a natural way.
</think>

The current local time is **July 1, 2025 at 12:33:59 AM**. Let me know if you need anything else! 😊
You: quit
```