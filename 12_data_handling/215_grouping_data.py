from itertools import groupby
from collections import defaultdict

orders = [
    {"product": "apple", "category": "fruit", "amount": 5},
    {"product": "banana", "category": "fruit", "amount": 3},
    {"product": "carrot", "category": "vegetable", "amount": 7},
    {"product": "broccoli", "category": "vegetable", "amount": 2},
    {"product": "cherry", "category": "fruit", "amount": 8},
]

by_category = defaultdict(list)
for order in orders:
    by_category[order["category"]].append(order)

for category, items in by_category.items():
    total = sum(i["amount"] for i in items)
    names = [i["product"] for i in items]
    print(f"{category}: {names}, total={total}")

sorted_orders = sorted(orders, key=lambda x: x["category"])
print("\nUsing itertools.groupby:")
for category, group in groupby(sorted_orders, key=lambda x: x["category"]):
    products = [o["product"] for o in group]
    print(f"  {category}: {products}")
