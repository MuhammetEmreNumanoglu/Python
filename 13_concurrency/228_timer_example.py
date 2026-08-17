import threading
import time

def run_after(delay, func, *args):
    timer = threading.Timer(delay, func, args)
    timer.start()
    return timer

def announce(message):
    print(f"[Timer] {message}")

print("Scheduling timers...")
t1 = run_after(0.5, announce, "Half second!")
t2 = run_after(1.0, announce, "One second!")
t3 = run_after(0.2, announce, "First!")

time.sleep(1.5)
print("All timers fired.")

class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

count = [0]

def tick():
    count[0] += 1
    print(f"Tick {count[0]}")

rt = RepeatTimer(0.3, tick)
rt.start()
time.sleep(1.2)
rt.cancel()
print("Stopped after", count[0], "ticks")
