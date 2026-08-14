import threading
import time

def download(url, duration):
    print(f"Downloading {url}...")
    time.sleep(duration)
    print(f"Done: {url}")

def greet(name, times):
    for i in range(times):
        print(f"Hello, {name}! ({i + 1})")
        time.sleep(0.1)

t1 = threading.Thread(target=download, args=("file1.zip", 0.3))
t2 = threading.Thread(target=download, args=("file2.zip", 0.2))
t3 = threading.Thread(target=greet, kwargs={"name": "Alice", "times": 3})

t1.start()
t2.start()
t3.start()

for t in [t1, t2, t3]:
    t.join()

print("All done.")
