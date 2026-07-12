import csv
import tempfile
import os

csv_file = os.path.join(tempfile.gettempdir(), "people.csv")

rows = [
    ["Name", "Age", "City"],
    ["Alice", 30, "London"],
    ["Bob", 25, "Paris"],
    ["Charlie", 35, "Tokyo"],
]

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Written.")

with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print()

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], "-", row["City"])

os.remove(csv_file)
