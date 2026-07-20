import sys

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

r = RegularPoint(1, 2)
s = SlottedPoint(1, 2)

print(r.x, r.y)
print(s.x, s.y)

r.z = 3
print(r.z)

try:
    s.z = 3
except AttributeError as e:
    print(f"Slots prevent new attributes: {e}")

print("Regular size:", sys.getsizeof(r.__dict__))
print("Slotted has no __dict__:", hasattr(s, "__dict__"))
