class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")

    def introduce(self):
        print(f"Hi, I'm {self.name}")

p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person.create_anonymous()

print("Population:", Person.get_population())
p3.introduce()

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

d = Date.from_string("2024-06-15")
print(d)
