class Dog:
    species = "Canis lupus familiaris"
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

d1 = Dog("Rex")
d2 = Dog("Buddy")
d3 = Dog("Max")

print(Dog.species)
print(Dog.count)

print(d1.name)
print(d1.species)

Dog.species = "Dog"
print(d1.species)
print(d2.species)
