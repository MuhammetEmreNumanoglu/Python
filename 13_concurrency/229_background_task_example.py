import threading
import time

def background_task(name, interval, stop_event):
    while not stop_event.is_set():
        print(f"[{name}] working...")
        time.sleep(interval)
    print(f"[{name}] stopped.")

stop = threading.Event()

t = threading.Thread(target=background_task, args=("BackgroundWorker", 0.3, stop))
t.daemon = True
t.start()

time.sleep(1.0)
stop.set()
t.join()
print("Main thread done.")
