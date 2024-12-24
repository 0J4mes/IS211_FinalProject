import sqlite3
from werkzeug.security import generate_password_hash

DB_PATH = './db/blog.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

username = "admin"  # Replace with your desired username
password = "admin123"  # Replace with your desired password

hashed_password = generate_password_hash(password)
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
conn.commit()
conn.close()

print("User added successfully!")
