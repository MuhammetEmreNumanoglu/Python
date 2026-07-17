class Car:
    def drive(self):
        print("Driving")

class Person:
    def greet(self):
        print("Hello!")

car1 = Car()
car2 = Car()
person = Person()

car1.drive()
car2.drive()
person.greet()

print(car1 is car2)
print(type(car1))
print(type(car1).__name__)
print(isinstance(car1, Car))
print(isinstance(car1, Person))
