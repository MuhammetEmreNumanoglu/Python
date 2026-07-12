import os
import tempfile
from pathlib import Path

temp_file = os.path.join(tempfile.gettempdir(), "delete_me.txt")

with open(temp_file, "w") as f:
    f.write("This file will be deleted")

print("Exists:", os.path.exists(temp_file))
os.remove(temp_file)
print("Deleted. Exists:", os.path.exists(temp_file))

temp2 = Path(tempfile.gettempdir()) / "delete_me2.txt"
temp2.write_text("Another file")
print("Exists:", temp2.exists())
temp2.unlink()
print("Deleted. Exists:", temp2.exists())

missing = Path(tempfile.gettempdir()) / "nonexistent.txt"
missing.unlink(missing_ok=True)
print("Safe delete of missing file: OK")
