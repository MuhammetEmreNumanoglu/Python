def process_order(items, discount=0):
    subtotal = sum(item["price"] * item["qty"] for item in items)
    print(f"[DEBUG] subtotal = {subtotal}")

    discount_amount = subtotal * discount
    print(f"[DEBUG] discount = {discount_amount}")

    total = subtotal - discount_amount
    print(f"[DEBUG] total = {total}")

    return total

items = [
    {"name": "apple", "price": 1.5, "qty": 3},
    {"name": "banana", "price": 0.8, "qty": 5},
    {"name": "cherry", "price": 3.0, "qty": 2},
]

total = process_order(items, discount=0.1)
print(f"Final total: ${total:.2f}")
