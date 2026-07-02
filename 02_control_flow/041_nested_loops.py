for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

for i in range(1, 6):
    print("*" * i)

multiplication_table = 3
for j in range(1, 11):
    print(f"{multiplication_table} x {j} = {multiplication_table * j}")
