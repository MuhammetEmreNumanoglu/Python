import time

print("Current time (epoch):", time.time())
print("Formatted:", time.ctime())

struct = time.localtime()
print("Year:", struct.tm_year)
print("Month:", struct.tm_mon)
print("Hour:", struct.tm_hour)

print("Sleeping for 1 second...")
start = time.time()
time.sleep(1)
elapsed = time.time() - start
print(f"Slept for {elapsed:.2f} seconds")

print(time.strftime("%Y-%m-%d %H:%M:%S"))
