import sqlite3

conn = sqlite3.connect("iare") # To connect to DB

cur = conn.cursor() # to get cursor object

cur.execute("") # To execute queries

result = cur.fetchall() # To fetch result
print(*result, sep="\n") # Printing result

conn.close() # Close DB connection