def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("count:", count)

    inner()
    inner()
    inner()
    print("final count:", count)

outer()

def make_counter():
    total = 0

    def add(n):
        nonlocal total
        total += n
        return total

    return add

counter = make_counter()
print(counter(5))
print(counter(3))
print(counter(10))
