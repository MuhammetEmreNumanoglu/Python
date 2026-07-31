from decimal import Decimal, getcontext

print(0.1 + 0.2)
print(Decimal("0.1") + Decimal("0.2"))

getcontext().prec = 6
result = Decimal("1") / Decimal("3")
print(result)

price = Decimal("19.99")
tax_rate = Decimal("0.18")
tax = price * tax_rate
total = price + tax

print(f"Price: {price}")
print(f"Tax: {tax.quantize(Decimal('0.01'))}")
print(f"Total: {total.quantize(Decimal('0.01'))}")

a = Decimal("10.5")
b = Decimal("3.2")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
