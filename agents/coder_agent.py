from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
 
 
class CoderAgent:
 
    def __init__(self):
        # Initialize LLM
        self.llm = ChatOllama(model="llama3")
 
    def generate_code(self, task, plan):
 
        print("[Coder] Generating Python code...\n")
 
        prompt = f"""
        You are an expert Python software engineer.
 
        Write Python code to solve the following task.
 
        Task:
        {task}
 
        Implementation Plan:
        {plan}
 
        Requirements:
        - Write clean Python code
        - Include a function definition
        - Do not include explanations
        - Output only the code
        """
 
        response = self.llm.invoke([HumanMessage(content=prompt)])
 
        return response.content