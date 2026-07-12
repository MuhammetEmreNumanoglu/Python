import os
import tempfile
from pathlib import Path

tmp = tempfile.gettempdir()

original = os.path.join(tmp, "original.txt")
renamed = os.path.join(tmp, "renamed.txt")

with open(original, "w") as f:
    f.write("content")

os.rename(original, renamed)
print("Renamed. Exists:", os.path.exists(renamed))

p = Path(renamed)
new_path = p.parent / "final.txt"
p.rename(new_path)
print("Renamed to:", new_path.name)
print("Exists:", new_path.exists())

new_path.unlink()
print("Cleaned up.")
