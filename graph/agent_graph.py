from typing import TypedDict
 
from langgraph.graph import StateGraph
 
from agents.planner_agent import PlannerAgent
from agents.coder_agent import CoderAgent
from agents.code_cleaner import CodeCleaner
from agents.tester_agent import TesterAgent
from agents.debugger_agent import DebuggerAgent
from tools.code_executor import CodeExecutor
 
 
# -------------------------------
# State
# -------------------------------
 
class AgentState(TypedDict):
    task: str
    plan: str
    code: str
    cleaned_code: str
    tests: str
    output: str
    errors: str
 
 
# -------------------------------
# Initialize Agents
# -------------------------------
 
planner = PlannerAgent()
coder = CoderAgent()
cleaner = CodeCleaner()
tester = TesterAgent()
debugger = DebuggerAgent()
executor = CodeExecutor()
 
 
# -------------------------------
# Nodes
# -------------------------------
 
def planner_node(state):
    print("\nPlanner Agent Creating Plan\n")
    plan = planner.create_plan(state["task"])
    print(plan)
    return {"plan": plan}
 
 
def coder_node(state):
    print("\nCoder Agent Writing Code\n")
    code = coder.generate_code(state["task"], state["plan"])
    print(code)
    return {"code": code}
 
 
def cleaner_node(state):
    print("\nCleaning Generated Code\n")
    cleaned = cleaner.clean_code(state["code"])
    print(cleaned)
    return {"cleaned_code": cleaned}
 
 
def tester_node(state):
    print("\nTester Agent Generating Tests\n")
    tests = tester.generate_tests(state["task"], state["cleaned_code"])
    cleaned_tests = cleaner.clean_code(tests)
    print(cleaned_tests)
    return {"tests": cleaned_tests}
 
 
def executor_node(state):
    print("\nRunning Tests...\n")
 
    full_code = state["cleaned_code"] + "\n\n" + state["tests"]
 
    output, errors = executor.execute_code(full_code)
 
    print(output)
    print(errors)
 
    return {
        "output": output,
        "errors": errors
    }
 
 
def debugger_node(state):
    print("\nDebugger Agent Fixing Code...\n")
 
    raw_fixed_code = debugger.fix_code(
        state["cleaned_code"],
        state["errors"],
        ""
    )
 
    # 🔥 IMPORTANT FIX: CLEAN AFTER DEBUGGER
    fixed_code = cleaner.clean_code(raw_fixed_code)
 
    print(fixed_code)
 
    return {"cleaned_code": fixed_code}
 
 
# -------------------------------
# Condition
# -------------------------------
 
def check_success(state):
    if "FAILED" in state["output"] or "Traceback" in state["errors"]:
        return "debugger"
    return "end"
 
 
# -------------------------------
# Graph
# -------------------------------
 
workflow = StateGraph(AgentState)
 
workflow.add_node("planner", planner_node)
workflow.add_node("coder", coder_node)
workflow.add_node("cleaner", cleaner_node)
workflow.add_node("tester", tester_node)
workflow.add_node("executor", executor_node)
workflow.add_node("debugger", debugger_node)
 
workflow.set_entry_point("planner")
 
workflow.add_edge("planner", "coder")
workflow.add_edge("coder", "cleaner")
workflow.add_edge("cleaner", "tester")
workflow.add_edge("tester", "executor")
 
# Conditional routing
workflow.add_conditional_edges(
    "executor",
    check_success,
    {
        "debugger": "debugger",
        "end": "__end__"
    }
)
 
# 🔥 FIXED LOOP
workflow.add_edge("debugger", "cleaner")   # critical fix
 
# Compile
agent_graph = workflow.compile()
 
