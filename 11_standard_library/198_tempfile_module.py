import tempfile
import os

with tempfile.TemporaryFile() as f:
    f.write(b"Hello, temp file!")
    f.seek(0)
    print(f.read())

with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
    f.write(b"Named temporary file")
    name = f.name

print("Temp file path:", name)
with open(name) as f:
    print(f.read())
os.remove(name)

with tempfile.TemporaryDirectory() as tmpdir:
    print("Temp dir:", tmpdir)
    file_path = os.path.join(tmpdir, "test.txt")
    with open(file_path, "w") as f:
        f.write("content")
    print("Files:", os.listdir(tmpdir))

print("Temp dir removed:", not os.path.exists(tmpdir))
