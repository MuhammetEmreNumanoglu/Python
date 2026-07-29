import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
print()

print(fibonacci.cache_info())

@functools.lru_cache(maxsize=128)
def expensive(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive(5))
print(expensive(5))
print(expensive(6))
print(expensive.cache_info())
