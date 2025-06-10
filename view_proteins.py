import sqlite3

conn = sqlite3.connect('proteins.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM proteins')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
