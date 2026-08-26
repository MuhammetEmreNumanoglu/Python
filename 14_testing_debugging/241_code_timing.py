import time

def slow_function():
    time.sleep(0.1)
    return sum(range(10000))

start = time.time()
result = slow_function()
end = time.time()
print(f"Result: {result}, Time: {end - start:.4f}s")

start_ns = time.perf_counter()
total = sum(i ** 2 for i in range(100000))
end_ns = time.perf_counter()
print(f"Sum: {total}, Time: {end_ns - start_ns:.4f}s")

def time_it(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"{func.__name__} took {elapsed:.4f}s")
    return result

time_it(sorted, list(range(10000, 0, -1)))
