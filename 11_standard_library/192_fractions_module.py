from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(1, 6)

print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(Fraction(0.1))
print(Fraction("0.1"))
print(Fraction("1/3"))

print(float(a))
print(a.numerator, a.denominator)

c = Fraction(3, 4)
d = Fraction(1, 4)
print(f"{c} + {d} = {c + d}")
print(f"{c} * {d} = {c * d}")
