class Shape:
    def area(self):
        return 0

    def describe(self):
        print(f"I am a shape with area {self.area():.2f}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def describe(self):
        print(f"I am a circle with radius {self.radius} and area {self.area():.2f}")

r = Rectangle(4, 5)
c = Circle(3)

r.describe()
c.describe()
print(r.area())
print(f"{c.area():.2f}")
