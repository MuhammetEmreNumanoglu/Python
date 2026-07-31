import functools

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(square(5))
print(cube(3))

def log(level, message):
    print(f"[{level}] {message}")

info = functools.partial(log, "INFO")
error = functools.partial(log, "ERROR")

info("Server started")
error("Connection failed")

multiply = lambda x, y: x * y
double = functools.partial(multiply, 2)
triple = functools.partial(multiply, 3)

print(list(map(double, [1, 2, 3, 4, 5])))
print(list(map(triple, [1, 2, 3, 4, 5])))
