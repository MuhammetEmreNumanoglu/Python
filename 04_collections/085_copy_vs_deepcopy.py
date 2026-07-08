import copy

original = [1, [2, 3], [4, 5]]

shallow = original.copy()
shallow[0] = 99
shallow[1].append(99)

print("Original:", original)
print("Shallow copy:", shallow)

original2 = [1, [2, 3], [4, 5]]
deep = copy.deepcopy(original2)
deep[0] = 99
deep[1].append(99)

print("Original2:", original2)
print("Deep copy:", deep)

d = {"a": [1, 2, 3]}
d_shallow = d.copy()
d_deep = copy.deepcopy(d)

d_shallow["a"].append(99)
print("Dict original:", d)
print("Dict shallow:", d_shallow)
print("Dict deep:", d_deep)
