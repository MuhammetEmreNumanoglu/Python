a, b, c = 1, 2, 3
print(a, b, c)

first, *rest = [1, 2, 3, 4, 5]
print(first, rest)

*beginning, last = [1, 2, 3, 4, 5]
print(beginning, last)

head, *middle, tail = [1, 2, 3, 4, 5]
print(head, middle, tail)

nested = (1, (2, 3), 4)
x, (y, z), w = nested
print(x, y, z, w)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(combined)

d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}
print(merged)
