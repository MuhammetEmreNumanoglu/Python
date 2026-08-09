import sqlite3
import tempfile
import os

db_path = os.path.join(tempfile.gettempdir(), "demo_insert.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

users = [("Charlie", 35), ("Dave", 28), ("Eve", 22)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)

conn.commit()
print("Inserted", cursor.rowcount, "rows in last batch")
print("Total rows:", conn.execute("SELECT COUNT(*) FROM users").fetchone()[0])

conn.close()
os.remove(db_path)
