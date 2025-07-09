#utility functions
def format_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def format_file_listing(name: str, size: int = None) -> str:
    if size is not None:
        return f"{name} ({format_size(size)})"
    else:
        return name


def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║              Directory Size Calculator Application           ║
║                                                              ║
║  A file system simulator with cd, ls, and size commands      ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner.strip()) 