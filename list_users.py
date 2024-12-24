import sqlite3

DB_PATH = './db/blog.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
conn.close()

print(users)
