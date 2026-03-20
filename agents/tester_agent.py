from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
 
 
class TesterAgent:
 
    def __init__(self):
        self.llm = ChatOllama(model="llama3")
 
    def generate_tests(self, task, code):
 
        prompt = f"""
You are a senior QA engineer.
 
Write Python unit tests for the given code.
 
IMPORTANT RULES:
- Do NOT import the function from another module
- Assume the function is already defined in the same file
- Only output executable Python code
- Do not include explanations
- Do not include markdown formatting
- Always include required imports such as:
    import unittest
    import sys
    from io import StringIO
 
Use the unittest framework.
 
Task:
{task}
 
Code:
{code}
"""
 
        response = self.llm.invoke([HumanMessage(content=prompt)])
 
        return response.content