x = 5
assert x > 0, "x must be positive"
print("x is positive:", x)

def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

print(divide(10, 2))

try:
    divide(10, 0)
except AssertionError as e:
    print(f"AssertionError: {e}")

data = [1, 2, 3, 4, 5]
assert len(data) > 0, "List must not be empty"
assert all(isinstance(n, int) for n in data), "All items must be integers"
print("Data is valid:", data)
