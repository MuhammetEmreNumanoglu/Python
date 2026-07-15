import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 100))
print(random.randrange(0, 100, 5))

items = ["apple", "banana", "cherry", "date"]
print(random.choice(items))
print(random.choices(items, k=3))

random.shuffle(items)
print(items)

print(random.sample(range(100), 5))

random.seed(42)
print(random.random())
random.seed(42)
print(random.random())
