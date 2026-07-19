class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"

animals = [Dog("Rex"), Cat("Whiskers"), Duck("Donald")]

for animal in animals:
    print(animal.speak())

def make_all_speak(animal_list):
    for a in animal_list:
        print(a.speak())

make_all_speak(animals)
