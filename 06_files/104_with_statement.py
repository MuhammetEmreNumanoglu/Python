import os
import tempfile

file_path = os.path.join(tempfile.gettempdir(), "test_with.txt")

with open(file_path, "w") as f:
    f.write("Hello from with statement\n")
    f.write("File closes automatically\n")

with open(file_path, "r") as f:
    data = f.read()
    print(data)

with open(file_path, "r") as f:
    lines = f.readlines()
    print("Lines:", lines)

print("File is closed:", f.closed)

os.remove(file_path)
