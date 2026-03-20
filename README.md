# Multi-Agent AI Coding System
 
This project is a multi-agent AI system that automatically:
- Plans a solution
- Generates code
- Cleans LLM output
- Creates test cases
- Executes code
- Debugs errors iteratively
 
## Architecture
 
Planner → Coder → Cleaner → Tester → Executor → Debugger → Cleaner → Executor
 
## Features
 
- Multi-agent architecture using LangGraph
- Automated test generation
- Self-debugging loop
- Handles syntax and logic errors
- Code cleaning to ensure executable outputs
 
## Tech Stack
 
- Python
- LangGraph
- LangChain
- Ollama (LLaMA3)
 
## How to Run
 
```bash
pip install -r requirements.txt
python run_agent.py
 