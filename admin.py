import sqlite3
from werkzeug.security import generate_password_hash

DB_PATH = './db/blog.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

username = "admin"
password = generate_password_hash("admin123")

cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
conn.commit()
conn.close()

print("Admin user created!")
