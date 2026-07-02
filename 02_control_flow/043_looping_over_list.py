numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num, end=" ")
print()

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print("Evens:", evens)

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

squared = [x ** 2 for x in numbers]
print("Squared:", squared)
