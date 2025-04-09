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

PRODUCTS_DATA = [("Salo", "100", "Made in Ukraine"), ("Cola", "100", "Made in US"), ("Beer", "100", "Made in Czech")]
CATEGORIES_DATA = [(1, "Food", "Much salt"), (2, "Drink", "Very sweet"), (3, "Alcohol", "Get relax")]


def create_product_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            product_price TEXT,
            product_description TEXT
            )
    ''')

def create_category_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            category_id INTEGER,
            category_name TEXT,
            category_description TEXT
            )
    ''')

def insert_products(cursor, product_name, product_price, product_description):
    cursor.execute('''
        INSERT INTO products (product_name, product_price, product_description) VALUES (?, ?, ?)
    ''', (product_name, product_price, product_description))

def insert_category(cursor, category_id, category_name, category_description):
    cursor.execute('''
        INSERT INTO categories (category_id, category_name, category_description) VALUES (?, ?, ?)
    ''', (category_id, category_name, category_description))


def get_products_info(cursor):
    all_data = cursor.execute(
        '''SELECT product_name, product_price, product_description, category_name, category_description
         from products JOIN categories ON products.id == categories.category_id
         ''')
    return all_data.fetchall()


def get_products(db_path):

    with ConnectDB(db_path) as conn:
        cursor = conn.cursor()

        create_product_table(cursor)
        for i in PRODUCTS_DATA:
            insert_products(cursor, *i)

        create_category_table(cursor)
        for i in CATEGORIES_DATA:
            insert_category(cursor, *i)

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
