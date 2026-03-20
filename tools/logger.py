import datetime
 
 
class AgentLogger:
 
    def __init__(self, log_file="agent_logs.txt"):
        self.log_file = log_file
 
    def log(self, message):
 
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
        log_message = f"[{timestamp}] {message}\n"
 
        with open(self.log_file, "a") as f:
            f.write(log_message)