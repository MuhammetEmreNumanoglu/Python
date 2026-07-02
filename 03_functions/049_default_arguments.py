def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def power(base, exponent=2):
    return base ** exponent

def create_profile(name, role="user", active=True):
    return {"name": name, "role": role, "active": active}

greet("Alice")
greet("Bob", "Hi")
greet("Charlie", greeting="Hey")

print(power(3))
print(power(3, 3))

print(create_profile("Alice"))
print(create_profile("Admin", role="admin"))
