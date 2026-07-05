def apply(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

print(apply(double, 5))
print(apply(square, 5))
print(apply(str.upper, "hello"))

def apply_all(funcs, value):
    for func in funcs:
        value = func(value)
    return value

result = apply_all([double, square, double], 3)
print(result)
