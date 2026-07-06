squares = [x ** 2 for x in range(10)]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)

pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)

names = ["Alice", "Bob", "Charlie", "Dave"]
long_names = [name for name in names if len(name) > 3]
print(long_names)
