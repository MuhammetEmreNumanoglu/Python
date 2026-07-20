class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower}hp) started")

class Wheels:
    def __init__(self, count):
        self.count = count

    def roll(self):
        print(f"{self.count} wheels rolling")

class Car:
    def __init__(self, make, horsepower, wheel_count):
        self.make = make
        self.engine = Engine(horsepower)
        self.wheels = Wheels(wheel_count)

    def drive(self):
        self.engine.start()
        self.wheels.roll()
        print(f"{self.make} is driving")

car = Car("Toyota", 150, 4)
car.drive()
print(f"HP: {car.engine.horsepower}")
print(f"Wheels: {car.wheels.count}")
