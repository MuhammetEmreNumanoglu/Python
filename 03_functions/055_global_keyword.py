counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(counter)

total = 100

def apply_discount(amount):
    global total
    total -= amount
    print(f"After discount: {total}")

apply_discount(20)
print("Final total:", total)
