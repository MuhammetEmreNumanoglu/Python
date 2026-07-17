class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.name)
print(alice.age)
print(bob.name)

alice.email = "alice@example.com"
print(alice.email)

print(alice.__dict__)
print(bob.__dict__)
