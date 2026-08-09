import sqlite3
import tempfile
import os

db_path = os.path.join(tempfile.gettempdir(), "demo.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
""")

conn.commit()
print("Database and table created.")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

conn.close()
os.remove(db_path)
