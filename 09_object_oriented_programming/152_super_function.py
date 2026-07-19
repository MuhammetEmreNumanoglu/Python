class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name}, age {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def describe(self):
        super().describe()
        print(f"Breed: {self.breed}")

class GuideDog(Dog):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed)
        self.owner = owner

    def describe(self):
        super().describe()
        print(f"Guide dog for: {self.owner}")

guide = GuideDog("Buddy", 3, "Labrador", "Alice")
guide.describe()
