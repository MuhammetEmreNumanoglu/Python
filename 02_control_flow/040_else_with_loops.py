for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop finished normally")

numbers = [1, 3, 5, 7]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in list")

count = 0
while count < 3:
    print("while:", count)
    count += 1
else:
    print("While loop finished")
