from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
 
 
class PlannerAgent:
 
    def __init__(self):
        # Initialize LLM
        self.llm = ChatOllama(model="llama3")
 
    def create_plan(self, task):
        
        print("[planner] Creating implementation plan...")
        
 
        prompt = f"""
        You are a senior software engineer.
 
        Break the following coding task into clear implementation steps.
        
        IMPORTANT:
        - prefer SIMPLE and READABLE solutions
        - Avoid complex algorithms unless absolutely necessary
        - Focus on correctness over optimization
        - The solution should be easy to implement and debug
        Task:
        {task}
 
        Provide numbered steps.
        """
 
        response = self.llm.invoke([HumanMessage(content=prompt)])
 
        return response.content
    
    