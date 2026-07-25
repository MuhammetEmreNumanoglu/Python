class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        return self.x != 0 or self.y != 0

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)
print(repr(v1))
print(v1 + v2)
print(len(v1))
print(v1[0], v1[1])
print(v1 == Vector(1, 2))
print(bool(Vector(0, 0)))
