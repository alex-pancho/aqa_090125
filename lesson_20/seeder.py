import sqlite3
from sqlite3 import Error

def insert_initial_data(conn):
    """Insert initial data into the database."""
    try:
        cursor = conn.cursor()

        # Insert sample categories
        categories = [
            ('Electronics',),
            ('Clothing',),
            ('Books',),
            ('Home & Kitchen',),
            ('Sports',)
        ]
        cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

        # Insert sample products
        products = [
            ('Smartphone', 'Latest model smartphone with advanced features.', 699.99, 1),
            ('T-shirt', 'Comfortable cotton t-shirt.', 19.99, 2),
            ('Novel', 'Bestselling novel of the year.', 14.99, 3),
            ('Blender', 'High-speed blender for smoothies and soups.', 49.99, 4),
            ('Soccer Ball', 'Official size soccer ball for training.', 29.99, 5)
        ]
        cursor.executemany("INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)", products)

        conn.commit()
        print("Initial data inserted successfully")
    except Error as e:
        print(f"Error: {e}")
