squares_gen = (x ** 2 for x in range(10))
print(type(squares_gen))

for sq in squares_gen:
    print(sq, end=" ")
print()

evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))

import sys

list_comp = [x ** 2 for x in range(1000)]
gen_exp = (x ** 2 for x in range(1000))

print("List size:", sys.getsizeof(list_comp))
print("Generator size:", sys.getsizeof(gen_exp))

total = sum(x ** 2 for x in range(100))
print("Sum of squares:", total)

any_negative = any(x < 0 for x in [1, 2, -3, 4])
print("Any negative:", any_negative)
