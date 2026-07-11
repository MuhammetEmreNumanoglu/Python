import os
import tempfile

sample_file = os.path.join(tempfile.gettempdir(), "sample.txt")

with open(sample_file, "w") as f:
    f.write("Hello from Python\nLine 2\nLine 3\n")

with open(sample_file, "r") as f:
    content = f.read()
    print(content)

with open(sample_file, "r") as f:
    content = f.read()
    print("Length:", len(content))

os.remove(sample_file)
