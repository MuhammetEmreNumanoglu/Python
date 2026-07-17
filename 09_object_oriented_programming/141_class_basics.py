class Dog:
    species = "Canis lupus familiaris"

    def bark(self):
        print("Woof!")

    def describe(self):
        print(f"I am a dog of species: {Dog.species}")

fido = Dog()
fido.bark()
fido.describe()
print(type(fido))
print(isinstance(fido, Dog))
