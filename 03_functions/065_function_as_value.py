def double(x):
    return x * 2

transform = double
print(transform(5))

operations = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
}

for name, func in operations.items():
    print(f"{name}(4) = {func(4)}")

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(double, 3))

functions = [str.upper, str.lower, str.title]
text = "hello WORLD"
for func in functions:
    print(func(text))
