a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference a-b:", a - b)
print("Difference b-a:", b - a)
print("Symmetric difference:", a ^ b)

print("Is subset:", {1, 2}.issubset(a))
print("Is superset:", a.issuperset({1, 2}))
print("Disjoint:", a.isdisjoint({10, 11}))

python_devs = {"Alice", "Bob", "Charlie"}
java_devs = {"Bob", "Dave", "Eve"}
both = python_devs & java_devs
print("Know both:", both)
