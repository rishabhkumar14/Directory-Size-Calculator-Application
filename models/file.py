# model for file
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        return f"{self.name} ({self.size})"
    
    def __repr__(self) -> str:
        return f"File(name='{self.name}', size={self.size})" 