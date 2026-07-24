import tempfile
import os

file_path = os.path.join(tempfile.gettempdir(), "ctx_demo.txt")

with open(file_path, "w") as f:
    f.write("Hello\n")

print("File closed after with block:", f.closed)

class Timer:
    import time as _time

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        return False

with Timer() as t:
    total = sum(range(1_000_000))

print(f"Sum computed in {t.elapsed:.4f}s")
os.remove(file_path)
