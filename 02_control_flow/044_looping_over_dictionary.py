person = {"name": "Alice", "age": 30, "city": "London"}

for key in person:
    print(key)

for key in person.keys():
    print(key, end=" ")
print()

for value in person.values():
    print(value, end=" ")
print()

for key, value in person.items():
    print(f"{key}: {value}")

scores = {"Math": 90, "English": 85, "Science": 92}
total = sum(scores.values())
print("Average:", total / len(scores))
