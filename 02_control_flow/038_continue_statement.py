for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

words = ["hello", "", "world", "", "python"]
for word in words:
    if word == "":
        continue
    print(word)

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
