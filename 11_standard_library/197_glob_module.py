import glob
import os

current_dir = os.path.dirname(__file__)

py_files = glob.glob(os.path.join(current_dir, "*.py"))
print(f"Python files in this directory: {len(py_files)}")
for f in sorted(py_files)[:5]:
    print(" ", os.path.basename(f))

all_files = glob.glob(os.path.join(current_dir, "1[89]*.py"))
for f in sorted(all_files):
    print(" ", os.path.basename(f))

parent = os.path.dirname(current_dir)
pattern = os.path.join(parent, "**", "*.py")
all_py = glob.glob(pattern, recursive=True)
print(f"\nTotal .py files in project: {len(all_py)}")
