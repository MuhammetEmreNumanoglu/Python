import os
import tempfile

file_path = os.path.join(tempfile.gettempdir(), "lines.txt")

with open(file_path, "w") as f:
    for i in range(1, 6):
        f.write(f"Line {i}: some content here\n")

with open(file_path, "r") as f:
    for line in f:
        print(line, end="")

print()

with open(file_path, "r") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.strip()}")

os.remove(file_path)
