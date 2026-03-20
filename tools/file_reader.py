class FileReaderTool:
 
    def read_file(self, filepath):
 
        try:
            with open(filepath, "r") as f:
                return f.read()
 
        except Exception as e:
            return str(e)