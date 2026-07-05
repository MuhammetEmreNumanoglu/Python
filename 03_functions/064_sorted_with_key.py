words = ["banana", "apple", "cherry", "date"]

print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

by_age = sorted(people, key=lambda p: p["age"])
for person in by_age:
    print(person)

pairs = [(1, "b"), (3, "a"), (2, "c")]
print(sorted(pairs, key=lambda x: x[1]))
