"""
    Створіть базу даних для інтернет-магазину з наступними таблицями:

    products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
    products: повинна мати зовнішній ключ на таблицю categories.
    categories: таблиця для категорій продуктів.
    
    Напишіть функції:
    1. для створення зазначених таблиць.
    2. Для Внесення декілька рядків даних в кожну таблицю
    3. JOIN-запит для повернення інформації про продукти та назву їх категорій

    Здати ЯК ПР. 
    Файл бази в ПР не включати.
"""
import sqlite3


def create_table_categories(cursor: sqlite3.Cursor):
    """Create tables categories for the online store database."""

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.connection.commit()


def create_table_products(cursor: sqlite3.Cursor):
    """Create tables products for the online store database."""

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            price REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')

    cursor.connection.commit()


def insert_sample_data_categories(cursor: sqlite3.Cursor, category: list):
    """Insert sample data into categories and products tables.
    Args:
        category: tuple list of category to insert.
    """
    
    cursor.executemany('''
        INSERT INTO categories (name) VALUES (?)
    ''', category)

    cursor.connection.commit()


def insert_sample_data_products(cursor: sqlite3.Cursor, products: list):
    """Insert sample data into categories and products tables.
    Args:
        products: tuple list of products to insert.
    """

    cursor.executemany('''
        INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)
    ''', products)

    cursor.connection.commit()


def get_products_with_categories(cursor: sqlite3.Cursor):
    """Retrieve products with their categories using JOIN."""

    cursor.execute('''
        SELECT products.name, products.description, products.price, categories.name
        FROM products
        JOIN categories ON products.category_id = categories.id
    ''')

    results = cursor.fetchall()
    return results



if __name__ == "__main__":
    
    with sqlite3.connect('store.db') as conn:
        cursor = conn.cursor()

    categories = [
        ('Electronics',),
        ('Clothing',),
        ('Books',)
    ]
    products = [
        ('Smartphone', 'Latest model smartphone', 699.99, 1),
        ('Laptop', 'High-performance laptop', 1299.99, 1),
        ('T-shirt', 'Comfortable cotton t-shirt', 19.99, 2),
        ('Novel', 'Bestselling novel', 14.99, 3)
    ]

    create_table_categories(cursor)
    create_table_products(cursor)
    insert_sample_data_categories(cursor, categories)
    insert_sample_data_products(cursor, products)
    products_with_categories = get_products_with_categories(cursor)
    for product in products_with_categories:
        print(f"Product: {product[0]}, Description: {product[1]}, Price: {product[2]}, Category: {product[3]}")
