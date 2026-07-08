from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

p = Point(3, 5)
print(p)
print(p.x, p.y)
print(p[0], p[1])

alice = Person("Alice", 30, "London")
print(alice)
print(alice.name)
print(alice._asdict())

updated = alice._replace(age=31)
print(updated)

print(Point._fields)
