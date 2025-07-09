from typing import Dict, Optional, Union
from .file import File

#model for directory
class Directory:
    def __init__(self, name: str, parent: Optional['Directory'] = None):
        self.name = name
        self.parent = parent
        self.children: Dict[str, Union[File, 'Directory']] = {}
    
    def add_file(self, name: str, size: int) -> File:
        file = File(name, size)
        self.children[name] = file
        return file
    
    def add_directory(self, name: str) -> 'Directory':
        directory = Directory(name, self)
        self.children[name] = directory
        return directory
    
    def get_child(self, name: str) -> Optional[Union[File, 'Directory']]:
        return self.children.get(name)
    
    def get_size(self) -> int:
        total = 0
        for child in self.children.values():
            total += child.get_size()
        return total
    
    def list_contents(self) -> list:
        return sorted(self.children.items())
    
    def __str__(self) -> str:
        return f"Directory: {self.name}"
    
    def __repr__(self) -> str:
        return f"Directory(name='{self.name}', children={len(self.children)})" 