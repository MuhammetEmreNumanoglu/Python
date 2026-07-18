class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    def display(self):
        print(f"{self._name}, age {self.__age}")

p = Person("Alice", 30)
p.display()
print(p.get_name())
print(p.get_age())

p.set_age(31)
p.display()

try:
    p.set_age(-1)
except ValueError as e:
    print(e)
