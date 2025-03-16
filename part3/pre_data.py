#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]


    db = MySQLdb.connect(
        host="localhost",
        port=5000,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    tabla = db.cursor()

    tabla.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id CHAR(36) PRIMARY KEY,  -- UUID format
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE
    );
    """)

    tabla.execute("""
    CREATE TABLE IF NOT EXISTS Place (
        id CHAR(36) PRIMARY KEY,  -- UUID format
        title VARCHAR(255) UNIQUE NOT NULL,
        description TEXT,
        price DECIMAL(10, 2),
        latitude FLOAT,
        longitude FLOAT,
        owner_id CHAR(36),  -- Foreign key referencing User(id)
        FOREIGN KEY (owner_id) REFERENCES User(id)
    );
    """)

    tabla.execute("""
    CREATE TABLE IF NOT EXISTS Review (
        id CHAR(36) PRIMARY KEY,  -- UUID format
        text TEXT NOT NULL,
        rating INT CHECK (rating BETWEEN 1 AND 5),
        user_id CHAR(36),  -- Foreign key referencing User(id)
        place_id CHAR(36),  -- Foreign key referencing Place(id)
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (place_id) REFERENCES Place(id),
        CONSTRAINT unique_review UNIQUE (user_id, place_id)
    );
    """)

    tabla.execute("""
    CREATE TABLE IF NOT EXISTS Amenity (
        id CHAR(36) PRIMARY KEY,  -- UUID format
        name VARCHAR(255) UNIQUE NOT NULL
    );
    """)

    tabla.execute("""
    CREATE TABLE IF NOT EXISTS Place_Amenity (
        place_id CHAR(36),
        amenity_id CHAR(36),
        PRIMARY KEY (place_id, amenity_id),
        FOREIGN KEY (place_id) REFERENCES Place(id),
        FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
    );
    """)

    tabla.execute("""
    INSERT IGNORE INTO Amenity (id, name)
    VALUES
    (UUID(), 'WiFi'),
    (UUID(), 'Swimming Pool'),
    (UUID(), 'Air Conditioning');
    """)


    db.commit()

    tabla.close()
    db.close()