items = ["a", "b", "c", "d", "e"]

print(items[0])
print(items[2])
print(items[-1])
print(items[-2])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][1])

words = ["hello", "world"]
print(words[0][1])

for i in range(len(items)):
    print(f"items[{i}] = {items[i]}")
