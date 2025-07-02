# Simple LLM Agent (with tools usage)
This is a library which contains boilerplate code/basic example of different ways to create your AI agent that uses custom tools and locally run llm model (ollama). You can easily modify it to use any other model as well.

Examples:
1. Langgraph Agent - Uses [Langgraph](https://www.langchain.com/langgraph) library and related langchain sum library for a basic reactive agent with simple tools.
2. More to come.

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

## Installing libraries
`uv add langgraph langchain_core langchain langchain-ollama`

## Running the agent
Comment/Uncomment the code to run specific Agent example in main.py.
Then run the main module main.py using
`uv run -m main`

or

`.\.venv\Scripts\python.exe main.py`

or to just run the langgraph module
`uv run -m langgraph_chat.chat_assitant`