import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "Alice", 30), (2, "Bob", 25), (3, "Charlie", 35)
])
conn.commit()

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
print("Updated:", cursor.rowcount, "row(s)")

cursor.execute("UPDATE users SET age = age + 1 WHERE age < 30")
print("Updated all under 30:", cursor.rowcount, "row(s)")
conn.commit()

cursor.execute("SELECT * FROM users")
print("After update:", cursor.fetchall())

cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
print("Deleted:", cursor.rowcount, "row(s)")
conn.commit()

cursor.execute("SELECT * FROM users")
print("After delete:", cursor.fetchall())

conn.close()
