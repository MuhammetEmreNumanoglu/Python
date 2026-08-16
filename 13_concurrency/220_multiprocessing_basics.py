import multiprocessing
import time
import os

def worker(name, seconds):
    pid = os.getpid()
    print(f"[{name}] PID={pid} starting")
    time.sleep(seconds)
    print(f"[{name}] PID={pid} done")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("Worker-1", 0.3))
    p2 = multiprocessing.Process(target=worker, args=("Worker-2", 0.2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main PID:", os.getpid())
    print("All done")
