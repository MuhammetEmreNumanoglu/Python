def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

for num in count_up(5):
    print(num, end=" ")
print()

gen = count_up(3)
print(type(gen))
print(next(gen))
print(next(gen))

counter = infinite_counter(10)
for _ in range(5):
    print(next(counter), end=" ")
print()
