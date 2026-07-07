point = (10, 20)
x, y = point
print(x, y)

first, second, third = (1, 2, 3)
print(first, second, third)

a, *rest = (1, 2, 3, 4, 5)
print(a)
print(rest)

*beginning, last = (1, 2, 3, 4, 5)
print(beginning)
print(last)

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

def get_user():
    return "Alice", 30, "London"

name, age, city = get_user()
print(name, age, city)
