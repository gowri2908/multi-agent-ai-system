from graph.agent_graph import agent_graph
 
 
task = "Write a Python code to find the longest palindrome in a string."
 
 
result = agent_graph.invoke(
    {
        "task": task
    }
)
 
print(result)



