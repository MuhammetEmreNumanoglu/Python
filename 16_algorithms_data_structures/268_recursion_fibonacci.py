from functools import lru_cache

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("Recursive (first 10):", [fibonacci_recursive(i) for i in range(10)])
print("Cached (first 15):", [fibonacci_cached(i) for i in range(15)])
print("Iterative (first 15):", [fibonacci_iterative(i) for i in range(15)])
