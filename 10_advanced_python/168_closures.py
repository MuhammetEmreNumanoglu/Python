def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = make_adder(10)
add_20 = make_adder(20)

print(add_10(5))
print(add_20(5))

print(double.__closure__)
print(double.__closure__[0].cell_contents)
