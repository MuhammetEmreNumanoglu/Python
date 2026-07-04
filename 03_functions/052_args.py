def total(*numbers):
    return sum(numbers)

def print_all(*args):
    for item in args:
        print(item)

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))

print_all("apple", "banana", "cherry")

def first_and_rest(first, *rest):
    print("First:", first)
    print("Rest:", rest)

first_and_rest(1, 2, 3, 4, 5)
