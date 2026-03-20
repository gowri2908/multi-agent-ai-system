import subprocess
 
 
class PackageInstallerTool:
 
    def install(self, package):
 
        try:
            subprocess.run(["pip", "install", package], check=True)
            return f"{package} installed successfully"
 
        except Exception as e:
            return str(e)
        
        