import bcrypt
import uuid
import sqlite3

sqliteConnection = sqlite3.connect('development.db')
cursor = sqliteConnection.cursor()
user_id = str(uuid.uuid4())
password = 'admin1234'
password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

cursor.execute("DROP TABLE IF EXISTS users;")
cursor.execute("DROP TABLE IF EXISTS amenities;")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);
"""

create_amenities_table = """
CREATE TABLE IF NOT EXISTS amenities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);
"""

cursor.execute(create_users_table)
cursor.execute(create_amenities_table)

user_table = """
INSERT INTO users(id, first_name, last_name, email, password, is_admin)
VALUES (?, ?, ?, ?, ?, ?);
"""

amenity_table = """
INSERT INTO amenities(id, name) 
VALUES (?, ?)
"""
user_data = (user_id, 'Admin', 'HBnB', 'admin@hbnb.io', password_hashed, True)
amenity_data = [
    (str(uuid.uuid4()), 'Wifi'),
    (str(uuid.uuid4()), 'Swimming Pool'),
    (str(uuid.uuid4()), 'Air Conditioning')
]

cursor.execute(user_table, user_data)
cursor.executemany(amenity_table, amenity_data)

sqliteConnection.commit()
cursor.close()
sqliteConnection.close()