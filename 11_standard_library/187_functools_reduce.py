import functools

numbers = [1, 2, 3, 4, 5]

total = functools.reduce(lambda acc, x: acc + x, numbers)
print("Sum:", total)

product = functools.reduce(lambda acc, x: acc * x, numbers)
print("Product:", product)

maximum = functools.reduce(lambda a, b: a if a > b else b, numbers)
print("Max:", maximum)

words = ["hello", " ", "world", "!"]
sentence = functools.reduce(lambda a, b: a + b, words)
print("Joined:", sentence)

result = functools.reduce(lambda acc, x: acc + x, [], 0)
print("Empty with initial:", result)
