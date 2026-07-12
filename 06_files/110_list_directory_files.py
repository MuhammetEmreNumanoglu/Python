import os
from pathlib import Path

cwd = Path(__file__).parent

print("Files in current directory:")
for item in os.listdir(cwd):
    full_path = cwd / item
    if full_path.is_file():
        size = full_path.stat().st_size
        print(f"  {item} ({size} bytes)")

print("\nAll .py files:")
for py_file in cwd.glob("*.py"):
    print(f"  {py_file.name}")

print("\nTotal files:", len([f for f in cwd.iterdir() if f.is_file()]))
