def describe(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe(name="Alice", age=30, city="London")
describe(age=25, city="Paris", name="Bob")
describe("Charlie", city="Tokyo", age=35)

def make_coffee(size, strength="medium", sugar=0):
    print(f"{size} coffee, {strength}, {sugar} sugar(s)")

make_coffee("large", sugar=2)
make_coffee(size="small", strength="strong")
