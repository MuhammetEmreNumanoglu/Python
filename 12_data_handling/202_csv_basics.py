import csv
import io

csv_data = """name,age,city
Alice,30,London
Bob,25,Paris
Charlie,35,Tokyo"""

reader = csv.DictReader(io.StringIO(csv_data))
for row in reader:
    print(f"{row['name']} ({row['age']}) - {row['city']}")

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "Alice", "score": 90})
writer.writerow({"name": "Bob", "score": 85})
print(output.getvalue())

rows = [["product", "price"], ["apple", 1.2], ["banana", 0.5]]
out2 = io.StringIO()
writer2 = csv.writer(out2)
writer2.writerows(rows)
print(out2.getvalue())
