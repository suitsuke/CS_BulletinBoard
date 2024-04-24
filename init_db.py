import sqlite3
from werkzeug.security import generate_password_hash
#for initializing hashed passwords

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

hash_value = generate_password_hash('kissa') #hash the password to not store in plaintext
cur.execute("INSERT INTO users (id, username, password, admin) VALUES (?, ?, ?, ?)",
            (1, 'maija', hash_value, 0)
            )
hash_value = generate_password_hash('Secur3Passwor#') #hash the password to not store in plaintext
cur.execute("INSERT INTO users (id, username, password, admin) VALUES (?, ?, ?, ?)",
            (0, 'admin', hash_value, 1)
            )
connection.commit()
connection.close()