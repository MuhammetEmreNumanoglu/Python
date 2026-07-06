fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(fruits)
print(numbers)
print(mixed)
print(len(fruits))
print(fruits[0])
print(fruits[-1])

fruits.append("date")
print(fruits)

fruits.remove("banana")
print(fruits)

print(sorted(numbers, reverse=True))
