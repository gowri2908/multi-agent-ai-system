import os
 
 
class CodeSearchTool:
 
    def search(self, directory, keyword):
 
        results = []
 
        for root, dirs, files in os.walk(directory):
 
            for file in files:
 
                if file.endswith(".py"):
 
                    path = os.path.join(root, file)
 
                    with open(path, "r") as f:
 
                        content = f.read()
 
                        if keyword in content:
                            results.append(path)
 
        return results