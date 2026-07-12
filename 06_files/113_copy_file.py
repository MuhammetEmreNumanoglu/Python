import shutil
import tempfile
import os
from pathlib import Path

tmp = tempfile.gettempdir()

source = os.path.join(tmp, "source.txt")
destination = os.path.join(tmp, "destination.txt")

with open(source, "w") as f:
    f.write("Original content\n")

shutil.copy(source, destination)
print("Copied.")
print("Source exists:", os.path.exists(source))
print("Dest exists:", os.path.exists(destination))

with open(destination) as f:
    print("Dest content:", f.read().strip())

shutil.copy2(source, os.path.join(tmp, "dest_with_meta.txt"))

os.remove(source)
os.remove(destination)
os.remove(os.path.join(tmp, "dest_with_meta.txt"))
print("Cleaned up.")
