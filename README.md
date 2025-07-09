# Directory Size Calculator Application

A modern Python application that simulates a file system with interactive commands for navigating directories and calculating sizes.

## Features

- **Interactive CLI**: Navigate through a simulated file system
- **Directory Navigation**: Use `cd` command to change directories
- **File Listing**: Use `ls` command to list directory contents
- **Size Calculation**: Use `size` command to calculate directory sizes
- **Human-readable Output**: File sizes are displayed in a user-friendly format
- **Clean Architecture**: Modular design with minimal, focused code

## Project Structure

```
Capgemini/
├── main.py              # Main application entry point
├── test.py              # Comprehensive test suite
├── README.md
├── models/              # Data models
│   ├── file.py          # File class
│   └── directory.py     # Directory class
├── filesystem/
│   ├── filesystem.py    # FileSystem class
│   └── initializer.py   # Seed data initializer
├── cli/
│   └── command_processor.py  # Command-line interface
└── utils/
    └── formatters.py    # Formatting utilities
```

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required. Just python.

## Usage

### Running the Application

Run the application:

```bash
python main.py
```

### Available Commands

- `cd <directory>` - Change to specified directory
- `cd ..` - Move up to the parent directory
- `cd /` - Return to the root directory
- `ls` - List contents of current directory
- `size` - Show total size of current directory
- `help` - Show help message
- `exit` - Exit the application

### Testing the Application

Run the comprehensive test suite to verify all functionality:

```bash
python test.py
```

The test suite covers:

- File and Directory models
- FileSystem operations (cd, ls, size)
- Command processing
- Formatting utilities
- Edge cases and error handling
- Sample filesystem structure validation

### Example Session

```
╔══════════════════════════════════════════════════════════════╗
║              Directory Size Calculator Application           ║
║                                                              ║
║  A file system simulator with cd, ls, and size commands      ║
╚══════════════════════════════════════════════════════════════╝

Type 'help' for available commands.

/> ls
documents
downloads
photos

/> cd documents
/documents> ls
notes.txt (512.0 B)
projects
report.txt (1.0 KB)

/documents> size
7.5 KB

/documents> cd projects
/documents/projects> ls
project1.doc (2.0 KB)
project2.doc (4.0 KB)

/documents/projects> exit
Goodbye!
```

## Architecture

### Models (`models/`)

- **File**: Represents a file with name and size
- **Directory**: Represents a directory containing files and subdirectories

### File System (`filesystem/`)

- **FileSystem**: Main file system simulator with navigation and operations

### CLI (`cli/`)

- **CommandProcessor**: Handles command parsing and execution

### Utils (`utils/`)

- **Formatters**: Utility functions for formatting output

## Benefits of This Structure

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Maintainability**: Easy to modify individual components
3. **Testability**: Each module can be tested independently
4. **Extensibility**: Easy to add new features or commands
5. **Type Hints**: Full type annotation support for better IDE experience
6. **Clean Code**: Minimal comments with self-documenting code

## Development

To extend the application:

1. **Add new commands**: Modify `cli/command_processor.py`
2. **Add new file system operations**: Modify `filesystem/filesystem.py`
3. **Add new formatting options**: Modify `utils/formatters.py`
4. **Add new data types**: Create new classes in `models/`

### Testing

- Run `python test.py` to execute all tests
- The test suite validates core functionality and edge cases
- Tests are organized by component for easy debugging
- All tests use assertions to verify expected behavior

## License

This project is open source and available under the MIT License.
