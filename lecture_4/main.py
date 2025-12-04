import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

with open('school.sql', 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()