class Person:
    def __init__(self, name, age, email=""):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1 = Person("Alice", 30, "alice@example.com")
p2 = Person("Bob", 25)

p1.introduce()
p2.introduce()

laptop = Product("Laptop", 999.99, 5)
print(f"{laptop.name}: ${laptop.total_value():.2f}")
