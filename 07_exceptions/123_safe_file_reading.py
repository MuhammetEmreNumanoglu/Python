import os

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except OSError as e:
        print(f"OS error: {e}")
    return None

content = read_file(__file__)
if content:
    print(f"Read {len(content)} characters from this file.")

result = read_file("/nonexistent/path.txt")
print("Result:", result)
