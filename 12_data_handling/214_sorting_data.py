people = [
    {"name": "Alice", "age": 30, "score": 92},
    {"name": "Charlie", "age": 25, "score": 85},
    {"name": "Bob", "age": 35, "score": 78},
    {"name": "Dave", "age": 28, "score": 95},
]

by_name = sorted(people, key=lambda p: p["name"])
print("By name:", [p["name"] for p in by_name])

by_score = sorted(people, key=lambda p: p["score"], reverse=True)
print("By score (desc):", [(p["name"], p["score"]) for p in by_score])

numbers = [5, 2, 8, 1, 9, 3, 7]
numbers.sort()
print("Sorted:", numbers)

words = ["banana", "apple", "cherry", "date"]
print("Sorted by length:", sorted(words, key=len))
print("Sorted alphabetically:", sorted(words))
