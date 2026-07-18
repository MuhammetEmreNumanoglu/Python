class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 5)
print(p)
print(str(p))
print(repr(p))

points = [Point(1, 2), Point(3, 4)]
print(points)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        return f"Temperature({self.celsius})"

t = Temperature(100)
print(t)
print(repr(t))
