from contextlib import contextmanager
import tempfile
import os

@contextmanager
def temporary_file(suffix=".txt"):
    path = tempfile.mktemp(suffix=suffix)
    try:
        yield path
    finally:
        if os.path.exists(path):
            os.remove(path)

with temporary_file() as tmp:
    with open(tmp, "w") as f:
        f.write("Temporary content\n")
    with open(tmp) as f:
        print(f.read())

print("File removed after context:", not os.path.exists(tmp))

@contextmanager
def section(title):
    print(f"--- {title} ---")
    yield
    print(f"--- End of {title} ---")

with section("Demo"):
    print("Doing some work...")
