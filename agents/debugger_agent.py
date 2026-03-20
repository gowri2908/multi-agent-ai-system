from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
 
from tools.file_reader import FileReaderTool
from tools.code_search import CodeSearchTool
from tools.package_installer import PackageInstallerTool
 
 
class DebuggerAgent:
 
    def __init__(self):
 
        self.llm = ChatOllama(model="llama3")
 
        self.file_reader = FileReaderTool()
        self.code_search = CodeSearchTool()
        self.installer = PackageInstallerTool()
 
    def fix_code(self, code, error, memory):
 
        prompt = f"""
You are a senior Python engineer.
 
The following code is failing test cases.
 
Previous attempts:
{memory}
 
Current code:
{code}
 
Error message:
{error}
 
Your task:
- Fix the code so that ALL test cases pass
- If the logic is incorrect, COMPLETELY REWRITE the function
- Do NOT try small fixes if logic is wrong
 
IMPORTANT:
- Prefer simple and correct solutions
- Handle all edge cases (like empty string)
- Ensure correctness over optimization
 
STRICT RULES:
- Return ONLY pure executable Python code
- Do NOT include markdown
- Do NOT include explanations
"""
 
 
        response = self.llm.invoke([HumanMessage(content=prompt)])
 
        return response.content
    

