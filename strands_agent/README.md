# Assistant using Strands Agents
This assistant is made using strands agents - an open source library to make agents with multiple llm providers.

References:
- https://strandsagents.com
- https://github.com/strands-agents/sdk-python
- https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/

We will use ollama as an example.

Update the ollama model as you like in code. I have used `qwen2.5:3b` by default

## Prerequisite
`uv add 'strands-agents[ollama]' 'strands_tools'`

### Ollama
Install ollama - 
Install ollama model with tooling support (https://ollama.com/blog/tool-support, https://ollama.com/search?c=tools)
- `ollama run qwen2.5:3b` pr `ollama run llama3.2`
It opens chat terminal which you can test for chatting or just close using `/bye`.

Start ollama server
- `ollama serve`

## Running assistant
`uv run -m strands_agent.chat_assistant`

### Example Conversation
```
You: Hello
Hello! How can I assist you today?

You: I am doing good how are you? Can you also tell me the time right now?

Tool #1: get_current_time
The current time is July 02, 2025, at 01:15:35. How can I assist you further?

You: What is result of 2*5*25/10 

Tool #2: calculator
The result of the expression \(2 \times 5 \times 25 / 10\) is 25. Is there anything else you would like to know or calculate?

You: Add 10 to the result

Tool #3: calculator
The result of adding 10 to the previous calculation \(2 \times 5 \times 25 / 10 + 10\) is 35. Is there anything else you would like to calculate or know?

You: quit
```