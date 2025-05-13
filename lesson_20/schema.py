import sqlite3
from sqlite3 import Error

def create_tables(conn):
    """Create tables in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        """)
        conn.commit()
        print("Tables created successfully")
    except Error as e:
        print(f"Error: {e}")
