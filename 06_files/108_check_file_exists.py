import os
from pathlib import Path

existing_file = Path(__file__)
missing_file = Path("/nonexistent/path/file.txt")

print(existing_file.exists())
print(missing_file.exists())

print(os.path.exists(str(existing_file)))
print(os.path.isfile(str(existing_file)))
print(os.path.isdir(str(existing_file.parent)))

def safe_read(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return None

result = safe_read(str(existing_file))
if result:
    print("File has", len(result), "characters")
