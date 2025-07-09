from typing import Optional
from models.directory import Directory
from utils.formatters import format_file_listing, format_size
from .initializer import FileSystemInitializer


class FileSystem:
    def __init__(self, root: Optional[Directory] = None):
        """
        Initialize the file system.
        
        Args:
            root: Optional root directory. If None, creates sample filesystem.
        """
        if root is None:
            self.root = FileSystemInitializer.create_sample_filesystem()
        else:
            self.root = root
        self.current = self.root
    
    def get_path(self) -> str:
        if self.current == self.root:
            return "/"
        
        path = []
        current = self.current
        while current != self.root:
            path.append(current.name)
            current = current.parent
        return "/" + "/".join(reversed(path))
    
    def cd(self, path: str) -> None:
        if not path:
            return
        
        if path == "/":
            self.current = self.root
        elif path == "..":
            if self.current.parent:
                self.current = self.current.parent
        else:
            child = self.current.get_child(path)
            if child and isinstance(child, Directory):
                self.current = child
            else:
                print(f"cd: no such directory: {path}")
    
    def ls(self) -> None:
        for name, child in self.current.list_contents():
            if hasattr(child, 'size'):
                print(format_file_listing(name, child.size))
            else:
                print(format_file_listing(name))
    
    def size(self) -> None:
        total_size = self.current.get_size()
        print(format_size(total_size)) 