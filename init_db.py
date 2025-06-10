import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('proteins.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS proteins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    accession TEXT UNIQUE,
    function TEXT,
    domains TEXT,
    crispr_score REAL,
    reference TEXT
)
''')

conn.commit()
conn.close()
