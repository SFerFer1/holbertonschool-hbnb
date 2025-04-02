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
CREATE TABLE IF NOT EXISTS user (
    id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);
"""

create_places_table = """
CREATE TABLE IF NOT EXISTS places (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36) NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);
"""
create_reviews_table ="""
CREATE TABLE IF NOT EXISTS reviews (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5) NOT NULL,
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    CONSTRAINT unique_user_place UNIQUE (user_id, place_id)
);
"""
create_amenities_table = """
CREATE TABLE IF NOT EXISTS amenity (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);
"""

cursor.execute(create_users_table)
cursor.execute(create_places_table)
cursor.execute(create_reviews_table)
cursor.execute(create_amenities_table)

user_table = """
INSERT INTO user(id, first_name, last_name, email, password, is_admin)
VALUES (?, ?, ?, ?, ?, ?);
"""

amenity_table = """
INSERT INTO amenity(id, name) 
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