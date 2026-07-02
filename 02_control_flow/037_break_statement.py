for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

numbers = [3, 7, 2, 9, 4, 1, 8]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print("Not found")

count = 0
while True:
    count += 1
    if count >= 5:
        break
print("Loop ended at count:", count)
