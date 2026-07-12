import os
import tempfile
from pathlib import Path

base = tempfile.gettempdir()

new_dir = os.path.join(base, "my_new_dir")
os.makedirs(new_dir, exist_ok=True)
print("Created:", new_dir)
print("Exists:", os.path.isdir(new_dir))

nested = os.path.join(base, "level1", "level2", "level3")
os.makedirs(nested, exist_ok=True)
print("Nested created:", nested)

path_dir = Path(base) / "pathlib_dir"
path_dir.mkdir(exist_ok=True)
print("Pathlib created:", path_dir)

os.rmdir(path_dir)
import shutil
shutil.rmtree(new_dir)
shutil.rmtree(os.path.join(base, "level1"))
print("Cleaned up.")
