import threading
import time

def print_numbers(name, count):
    for i in range(1, count + 1):
        print(f"[{name}] {i}")
        time.sleep(0.1)

t1 = threading.Thread(target=print_numbers, args=("Thread-1", 3))
t2 = threading.Thread(target=print_numbers, args=("Thread-2", 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads done.")
print("Active threads:", threading.active_count())
