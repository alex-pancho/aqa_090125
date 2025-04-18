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
from pathlib import Path

DB_PATH = Path("market.db")

PRODUCTS_DATA = [
    ("Tent", 1500, "Durable tent for outdoor adventures", 1),
    ("Sleeping Bag", 800, "Comfortable sleeping bag for cold nights", 1),
    ("Hiking Boots", 1200, "High-quality boots for hiking in rough terrains", 1),
    ("Travel Guide", 500, "Comprehensive guide to explore Europe", 2),
    ("Travel Insurance", 1000, "Comprehensive insurance for international travel", 2),
    ("Camera", 2500, "High-resolution camera for travel photography", 3)
]

CATEGORIES_DATA = [
    (1, "Camping Gear", "All necessary equipment for outdoor camping"),
    (2, "Travel Essentials", "Everything you need for safe and enjoyable travels"),
    (3, "Travel Photography", "Capture the best moments of your travels")
]


def create_product_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            product_price REAL,  -- Changed to REAL for price
            product_description TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

def create_category_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            category_name TEXT,
            category_description TEXT
        )
    ''')

def insert_products(cursor, product_name, product_price, product_description, category_id):
    cursor.execute('''
        INSERT OR IGNORE INTO products (product_name, product_price, product_description, category_id) 
        VALUES (?, ?, ?, ?)
    ''', (product_name, product_price, product_description, category_id))

def insert_category(cursor, category_id, category_name, category_description):
    cursor.execute('''
        INSERT OR IGNORE INTO categories (id, category_name, category_description) 
        VALUES (?, ?, ?)
    ''', (category_id, category_name, category_description))


def get_products_info(cursor):
    all_data = cursor.execute(
        '''SELECT product_name, product_price, product_description, category_name, category_description
           FROM products 
           JOIN categories ON products.category_id = categories.id
        ''')
    return all_data.fetchall()


def get_products(db_path):

    with ConnectDB(db_path) as conn:
        cursor = conn.cursor()

        create_category_table(cursor)
        for i in CATEGORIES_DATA:
            insert_category(cursor, *i)

        create_product_table(cursor)
        for i in PRODUCTS_DATA:
            insert_products(cursor, *i)

        return get_products_info(cursor)


class ConnectDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()


if __name__ == '__main__':
    print(get_products(DB_PATH))