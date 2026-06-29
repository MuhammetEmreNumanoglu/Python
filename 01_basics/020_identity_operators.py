a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)

x = None
print(x is None)
print(x is not None)

name = "Alice"
same_name = "Alice"
print(name is same_name)
