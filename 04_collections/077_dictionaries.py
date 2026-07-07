person = {"name": "Alice", "age": 30, "city": "London"}

print(person)
print(person["name"])
print(person.get("email", "N/A"))

person["email"] = "alice@example.com"
person["age"] = 31
print(person)

del person["city"]
print(person)

print("name" in person)
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))
