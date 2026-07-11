import os
import tempfile

output_file = os.path.join(tempfile.gettempdir(), "output.txt")

with open(output_file, "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("File written.")

with open(output_file, "r") as f:
    print(f.read())

with open(output_file, "w") as f:
    f.write("Overwritten content\n")

with open(output_file, "r") as f:
    print(f.read())

os.remove(output_file)
