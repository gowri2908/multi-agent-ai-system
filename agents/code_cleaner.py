import re
 
class CodeCleaner:
 
    def clean_code(self, code):
        # Remove markdown blocks like ```python or ```
        code = re.sub(r"```[a-zA-Z]*", "", code)
        code = re.sub(r"```", "", code)
 
        # Remove unwanted explanation lines
        lines = code.split("\n")
        cleaned_lines = []
 
        for line in lines:
            if any(keyword in line.lower() for keyword in [
                "here is", "solution", "explanation"
            ]):
                continue
            cleaned_lines.append(line)
 
        return "\n".join(cleaned_lines)