import threading

counter_unsafe = 0
counter_safe = 0
lock = threading.Lock()

def unsafe_increment():
    global counter_unsafe
    for _ in range(10000):
        counter_unsafe += 1

def safe_increment():
    global counter_safe
    for _ in range(10000):
        with lock:
            counter_safe += 1

threads_unsafe = [threading.Thread(target=unsafe_increment) for _ in range(5)]
threads_safe = [threading.Thread(target=safe_increment) for _ in range(5)]

for t in threads_unsafe:
    t.start()
for t in threads_unsafe:
    t.join()

for t in threads_safe:
    t.start()
for t in threads_safe:
    t.join()

print(f"Expected: 50000")
print(f"Unsafe counter (may be wrong): {counter_unsafe}")
print(f"Safe counter (always correct): {counter_safe}")
