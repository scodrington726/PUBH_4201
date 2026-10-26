
import sqlite3

conn = sqlite3.connect("cohort.db")

with open("queries.sql", "r") as file:
    sql = file.read()

queries = [q.strip() for q in sql.split(";") if q.strip()]

for i, query in enumerate(queries, start=1):
    results = conn.execute(query).fetchall()

    print(f"\nTask 2 - Query {i}")
    print("Number of rows returned:", len(results))
    print("First 10 rows:")

    for row in results[:10]:
        print(row)

conn.close()

