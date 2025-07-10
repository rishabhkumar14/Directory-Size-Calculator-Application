#!/usr/bin/env python3
"""
Test suite for Directory Size Calculator

This file contains comprehensive tests for all major functionality:
- File and Directory models
- FileSystem operations (cd, ls, size)
- Command processing
- Formatting utilities
- Edge cases and error handling

Run with: python test.py
"""

import sys
import os

# Add the current directory to Python path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.file import File
from models.directory import Directory
from filesystem.filesystem import FileSystem
from filesystem.initializer import FileSystemInitializer
from cli.command_processor import CommandProcessor
from utils.formatters import format_size, format_file_listing


def test_file_model():
    """Test File model functionality"""
    print("Testing File model...")
    
    # Test basic file creation
    file1 = File("test.txt", 1024)
    assert file1.name == "test.txt"
    assert file1.size == 1024
    assert file1.get_size() == 1024
    
    # Test file string representation
    assert str(file1) == "test.txt (1024)"
    assert "test.txt" in repr(file1)
    
    print("✓ File model tests passed")


def test_directory_model():
    """Test Directory model functionality"""
    print("Testing Directory model...")
    
    # Test basic directory creation
    root = Directory("root")
    assert root.name == "root"
    assert len(root.children) == 0
    
    # Test adding files
    file1 = root.add_file("test.txt", 512)
    assert "test.txt" in root.children
    assert root.get_size() == 512
    
    # Test adding directories
    subdir = root.add_directory("subdir")
    assert "subdir" in root.children
    assert subdir.parent == root
    
    # Test nested structure
    subdir.add_file("nested.txt", 256)
    assert root.get_size() == 768  # 512 + 256
    
    # Test get_child
    assert root.get_child("test.txt") == file1
    assert root.get_child("subdir") == subdir
    assert root.get_child("nonexistent") is None
    
    # Test list_contents
    contents = root.list_contents()
    assert len(contents) == 2
    assert contents[0][0] == "subdir"  # sorted alphabetically
    assert contents[1][0] == "test.txt"
    
    print("✓ Directory model tests passed")


def test_filesystem_operations():
    """Test FileSystem operations"""
    print("Testing FileSystem operations...")
    
    # Create a simple filesystem for testing
    root = Directory("/")
    docs = root.add_directory("documents")
    docs.add_file("report.txt", 1024)
    docs.add_file("notes.txt", 512)
    
    projects = docs.add_directory("projects")
    projects.add_file("project1.doc", 2048)
    
    fs = FileSystem(root)
    
    # Test initial state
    assert fs.current == root
    assert fs.get_path() == "/"
    
    # Test cd operations
    fs.cd("documents")
    assert fs.current == docs
    assert fs.get_path() == "/documents"
    
    fs.cd("projects")
    assert fs.current == projects
    assert fs.get_path() == "/documents/projects"
    
    # Test cd to parent
    fs.cd("..")
    assert fs.current == docs
    assert fs.get_path() == "/documents"
    
    # Test cd to root
    fs.cd("/")
    assert fs.current == root
    assert fs.get_path() == "/"
    
    # Test cd to nonexistent directory
    fs.cd("nonexistent")
    assert fs.current == root  # Should stay in current directory
    
    # Test size calculation
    assert docs.get_size() == 3584  # 1024 + 512 + 2048
    
    print("✓ FileSystem operations tests passed")


def test_command_processor():
    """Test CommandProcessor functionality"""
    print("Testing CommandProcessor...")
    
    fs = FileSystem()
    processor = CommandProcessor(fs)
    
    # Test help command
    result = processor.process_command(["help"])
    assert result is True
    
    # Test ls command
    result = processor.process_command(["ls"])
    assert result is True
    
    # Test size command
    result = processor.process_command(["size"])
    assert result is True
    
    # Test cd command
    result = processor.process_command(["cd", "documents"])
    assert result is True
    
    # Test exit command
    result = processor.process_command(["exit"])
    assert result is False
    
    # Test unknown command
    result = processor.process_command(["unknown"])
    assert result is True
    
    # Test empty command
    result = processor.process_command([])
    assert result is True
    
    print("✓ CommandProcessor tests passed")


def test_formatters():
    """Test formatting utilities"""
    print("Testing formatters...")
    
    # Test size formatting
    assert format_size(0) == "0 B"
    assert format_size(512) == "512.0 B"
    assert format_size(1024) == "1.0 KB"
    assert format_size(1048576) == "1.0 MB"
    assert format_size(1073741824) == "1.0 GB"
    
    # Test file listing formatting
    assert format_file_listing("test.txt", 1024) == "test.txt (1.0 KB)"
    assert format_file_listing("folder") == "folder"
    
    print("✓ Formatter tests passed")


def test_sample_filesystem():
    """Test the sample filesystem structure"""
    print("Testing sample filesystem...")
    
    root = FileSystemInitializer.create_sample_filesystem()
    
    # Test root structure
    assert root.name == "/"
    assert "documents" in root.children
    assert "downloads" in root.children
    assert "photos" in root.children
    
    # Test documents structure
    documents = root.get_child("documents")
    assert isinstance(documents, Directory)
    assert "report.txt" in documents.children
    assert "notes.txt" in documents.children
    assert "projects" in documents.children
    
    # Test nested structure
    projects = documents.get_child("projects")
    assert "project1.doc" in projects.children
    assert "project2.doc" in projects.children
    
    # Test file sizes
    assert documents.get_child("report.txt").get_size() == 1024
    assert documents.get_child("notes.txt").get_size() == 512
    assert projects.get_child("project1.doc").get_size() == 2048
    assert projects.get_child("project2.doc").get_size() == 4096
    
    # Test total size calculation
    total_docs_size = documents.get_size()
    assert total_docs_size == 7680  # 1024 + 512 + 2048 + 4096
    
    print("✓ Sample filesystem tests passed")


def test_edge_cases():
    """Test edge cases and error handling"""
    print("Testing edge cases...")
    
    # Test empty directory
    empty_dir = Directory("empty")
    assert empty_dir.get_size() == 0
    assert len(empty_dir.list_contents()) == 0
    
    # Test large file sizes
    large_file = File("large.dat", 1099511627776)  # 1 TB
    assert large_file.get_size() == 1099511627776
    assert "TB" in format_size(large_file.get_size())
    
    # Test filesystem with empty path
    fs = FileSystem()
    fs.cd("")  # Should not change directory
    assert fs.current == fs.root
    
    # Test directory with special characters
    special_dir = Directory("test-dir_123")
    assert special_dir.name == "test-dir_123"
    
    print("✓ Edge cases tests passed")


def get_available_tests():
    """Return a dictionary of available test functions"""
    return {
        "1": ("File Model", test_file_model),
        "2": ("Directory Model", test_directory_model),
        "3": ("FileSystem Operations", test_filesystem_operations),
        "4": ("Command Processor Test", test_command_processor),
        "5": ("Formatters", test_formatters),
        "6": ("Sample Filesystem", test_sample_filesystem),
        "7": ("Edge Cases", test_edge_cases),
    }


def display_test_menu():
    """Display the test selection menu"""
    print("=" * 60)
    print("Directory Size Calculator - Test Suite")
    print("=" * 60)
    print()
    print("Available tests:")
    print()
    
    tests = get_available_tests()
    for key, (name, _) in tests.items():
        print(f"  {key}. {name}")
    
    print()
    print("Please type one of the following:")
    print("  • A number (1-7) to run a specific test")
    print("  • 'all' to run all tests")
    print("  • 'exit' to quit the test suite")
    print()


def run_specific_test(test_func, test_name):
    """Run a specific test function"""
    print(f"\n{'='*20} {test_name} {'='*20}")
    try:
        test_func()
        print(f"✓ {test_name} passed successfully!")
        return True
    except AssertionError as e:
        print(f"❌ {test_name} failed!")
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"❌ {test_name} encountered an unexpected error!")
        print(f"Error: {e}")
        return False


def run_all_tests():
    """Run all test functions"""
    print("=" * 60)
    print("Running ALL Directory Size Calculator Tests")
    print("=" * 60)
    print()
    
    tests = get_available_tests()
    passed = 0
    total = len(tests)
    
    for key, (name, test_func) in tests.items():
        if run_specific_test(test_func, name):
            passed += 1
    
    print()
    print("=" * 60)
    if passed == total:
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 60)
        print()
        print("The application is working correctly.")
        print("You can now run 'python main.py' to use the interactive CLI.")
    else:
        print(f"❌ {passed}/{total} TESTS PASSED")
        print("=" * 60)
        print()
        print("Some tests failed. Please check the errors above.")


def interactive_test_runner():
    """Interactive test runner that allows users to choose tests"""
    while True:
        display_test_menu()
        
        choice = input("Enter your choice (number 1-7, 'all', or 'exit'): ").strip().lower()
        
        if choice == "exit":
            print("\nExiting test suite. Goodbye!")
            break
        elif choice == "all":
            run_all_tests()
            break
        else:
            tests = get_available_tests()
            if choice in tests:
                name, test_func = tests[choice]
                run_specific_test(test_func, name)
                
                # Ask if user wants to run another test
                another = input("\nRun another test? (y/n): ").strip().lower()
                if another not in ['y', 'yes']:
                    print("\nExiting test suite. Goodbye!")
                    break
            else:
                print(f"\n❌ Invalid choice: '{choice}'. Please try again.\n")


if __name__ == "__main__":
    interactive_test_runner() 