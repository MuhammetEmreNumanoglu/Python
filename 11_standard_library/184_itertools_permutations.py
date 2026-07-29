import itertools

items = ["a", "b", "c"]

all_perms = list(itertools.permutations(items))
print("All permutations of 3:", all_perms)
print("Count:", len(all_perms))

perms_2 = list(itertools.permutations(items, 2))
print("P(3,2):", perms_2)

digits = [1, 2, 3]
perms = list(itertools.permutations(digits))
numbers = [int("".join(map(str, p))) for p in perms]
print("All 3-digit numbers from 1,2,3:", numbers)
