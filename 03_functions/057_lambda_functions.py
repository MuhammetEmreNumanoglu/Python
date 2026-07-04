square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print(square(5))
print(add(3, 7))
print(is_even(4))

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort(key=lambda x: x)
print(numbers)

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
people.sort(key=lambda person: person[1])
print(people)

evens = list(filter(lambda n: n % 2 == 0, range(10)))
print(evens)
