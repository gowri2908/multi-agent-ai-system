import subprocess
import tempfile
import os
 
 
class CodeExecutor:
 
    def execute_code(self, code):
 
        try:
            # Create temporary file to store generated code
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as temp_file:
                temp_file.write(code)
                temp_file_path = temp_file.name
 
            # Execute the Python file
            result = subprocess.run(
                ["python", temp_file_path],
                capture_output=True,
                text=True
            )
 
            output = result.stdout
            errors = result.stderr
 
            # Delete the temporary file
            os.remove(temp_file_path)
 
            return output, errors
 
        except Exception as e:
            return "", str(e)
 