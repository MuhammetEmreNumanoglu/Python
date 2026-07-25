class Celsius:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        obj.__dict__[self.name] = value

class Temperature:
    celsius = Celsius()

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

t = Temperature(100)
print(t.celsius)
print(t.fahrenheit)

t.celsius = -10
print(t.celsius)

try:
    t.celsius = -300
except ValueError as e:
    print(e)
