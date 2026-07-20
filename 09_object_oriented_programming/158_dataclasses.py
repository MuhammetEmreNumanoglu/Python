from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Person:
    name: str
    age: int
    email: str = ""
    hobbies: list = field(default_factory=list)

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

p = Point(3.0, 5.0)
print(p)
print(p.x)

alice = Person("Alice", 30, "alice@example.com", ["reading", "coding"])
print(alice)
alice.introduce()

bob = Person("Bob", 25)
print(bob)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
