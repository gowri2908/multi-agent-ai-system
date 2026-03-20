class AgentMemory:
 
    def __init__(self):
        self.memory = []
 
    def add(self, entry):
        self.memory.append(entry)
 
    def get_memory(self):
        return "\n".join(self.memory)
 