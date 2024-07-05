import os

def list_directory_contents(path):
    try:
        # Get the list of all files and directories
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Example usage
list_directory_contents('.')  # Lists contents of the current directory
