from filesystem.filesystem import FileSystem
from cli.command_processor import CommandProcessor
from utils.formatters import print_banner


def main():
    fs = FileSystem()
    processor = CommandProcessor(fs)
    
    print_banner()
    print("Type 'help' for available commands.")
    print()
    
    while True:
        try:
            prompt = processor.get_prompt()
            command = input(prompt).strip().split()
            
            should_continue = processor.process_command(command)
            
            if not should_continue:
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()