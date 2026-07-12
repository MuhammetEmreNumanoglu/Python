from pathlib import Path

home = Path.home()
print("Home:", home)

cwd = Path.cwd()
print("CWD:", cwd)

file_path = home / "Documents" / "notes.txt"
print("Path:", file_path)
print("Name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)
print("Parent:", file_path.parent)
print("Exists:", file_path.exists())

temp = Path.home() / "temp_pathlib_demo.txt"
temp.write_text("Hello from pathlib!")
print("Content:", temp.read_text())
temp.unlink()

docs = home / "Documents"
if docs.exists():
    py_files = list(docs.glob("*.py"))
    print("Python files:", py_files[:3])
