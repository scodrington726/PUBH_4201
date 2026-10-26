
import sqlite3

# Connect to the database
conn = sqlite3.connect("cohort.db")
cursor = conn.cursor()

# Find all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\nTABLE: {table_name}")

    # Get the number of rows
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    print("Rows:", cursor.fetchone()[0])

    # Get the columns
    cursor.execute(f"PRAGMA table_info({table_name})")
    for column in cursor.fetchall():
        print("Column:", column[1], "| Type:", column[2])

    # Get foreign keys
    cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    print("Foreign keys:", cursor.fetchall())

conn.close()
