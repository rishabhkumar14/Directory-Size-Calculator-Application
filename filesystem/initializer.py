from typing import Dict, Any
from models.directory import Directory
from models.file import File


class FileSystemInitializer:
    """Handles initialization and population of the file system with sample data."""
    
    @staticmethod
    def create_sample_filesystem() -> Directory:
    
        root = Directory("/")
        
        # Create main directories
        documents = root.add_directory("documents")
        downloads = root.add_directory("downloads")
        photos = root.add_directory("photos")
        
        # Populate documents
        documents.add_file("report.txt", 1024)
        documents.add_file("notes.txt", 512)
        
        projects = documents.add_directory("projects")
        projects.add_file("project1.doc", 2048)
        projects.add_file("project2.doc", 4096)
        
        # Populate downloads
        downloads.add_file("installer.exe", 1048576)
        downloads.add_file("document.pdf", 524288)
        
        # Populate photos
        photos.add_file("vacation1.jpg", 3145728)
        photos.add_file("vacation2.jpg", 2097152)
        
        albums = photos.add_directory("albums")
        summer = albums.add_directory("summer")
        summer.add_file("beach1.jpg", 1048576)
        summer.add_file("beach2.jpg", 1048576)
        
        return root 