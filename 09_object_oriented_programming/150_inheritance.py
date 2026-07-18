class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        print(f"I am {self.name}")

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def fetch(self):
        print(f"{self.name} fetches the ball!")

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.describe()
print(dog.speak())
dog.fetch()

cat.describe()
print(cat.speak())

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
