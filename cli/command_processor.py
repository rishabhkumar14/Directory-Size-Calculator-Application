from typing import List
from filesystem.filesystem import FileSystem


class CommandProcessor:
    def __init__(self, filesystem: FileSystem):
        self.filesystem = filesystem
    
    def process_command(self, command_parts: List[str]) -> bool:
        if not command_parts:
            return True
        
        cmd = command_parts[0].lower()
        
        if cmd == "cd" and len(command_parts) > 1:
            self.filesystem.cd(command_parts[1])
        elif cmd == "ls":
            self.filesystem.ls()
        elif cmd == "size":
            self.filesystem.size()
        elif cmd == "exit":
            return False
        elif cmd == "help":
            self._show_help()
        else:
            print(f"Unknown command: {cmd}")
            print("Type 'help' for available commands.")
        
        return True
    
    def _show_help(self):
        help_text = """
Available Commands:
  cd <directory>  - Change to specified directory
  ls              - List contents of current directory
  size            - Show total size of current directory
  help            - Show this help message
  exit            - Exit the application
        """
        print(help_text.strip())
    
    def get_prompt(self) -> str:
        return f"{self.filesystem.get_path()}> " 