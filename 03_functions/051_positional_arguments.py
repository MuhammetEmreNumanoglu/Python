def add(a, b):
    return a + b

def describe(name, age):
    print(f"{name} is {age}")

print(add(10, 5))
describe("Alice", 30)

values = [3, 7]
print(add(*values))

data = {"name": "Bob", "age": 25}
describe(**data)
