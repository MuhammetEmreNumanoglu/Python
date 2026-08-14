import threading
import time

counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Expected:", 5000)
print("Got:", counter)

shared_list = []
list_lock = threading.Lock()

def add_items(items):
    for item in items:
        with list_lock:
            shared_list.append(item)

t1 = threading.Thread(target=add_items, args=(range(5),))
t2 = threading.Thread(target=add_items, args=(range(5, 10),))
t1.start(); t2.start()
t1.join(); t2.join()
print("Shared list length:", len(shared_list))
