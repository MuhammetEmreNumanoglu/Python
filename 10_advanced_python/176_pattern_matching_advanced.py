from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float

shape = Circle(Point(0, 0), 5)

match shape:
    case Circle(center=Point(x=0, y=0), radius=r):
        print(f"Circle at origin with radius {r}")
    case Circle(center=Point(x=x, y=y), radius=r):
        print(f"Circle at ({x},{y}) with radius {r}")

data = {"type": "user", "name": "Alice", "role": "admin"}

match data:
    case {"type": "user", "name": name, "role": "admin"}:
        print(f"Admin user: {name}")
    case {"type": "user", "name": name}:
        print(f"Regular user: {name}")
    case _:
        print("Unknown")

values = [1, 2, 3]
match values:
    case [first, *rest] if first > 0:
        print(f"Positive list starting with {first}, rest={rest}")
