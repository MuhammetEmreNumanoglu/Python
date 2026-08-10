import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "Alice", 30), (2, "Bob", 25), (3, "Charlie", 35), (4, "Dave", 28)
])
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.execute("SELECT name, age FROM users WHERE age > ?", (27,))
for row in cursor.fetchall():
    print(row)

conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(f"{row['name']}: {row['age']}")

conn.close()
