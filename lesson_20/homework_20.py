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

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)    
        )
''')
    conn.commit()

def insert_data(conn, categories, products):
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO categories (name) VALUES (?)', categories)
    cursor.executemany(
        'INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)', products
        )
    
    conn.commit()

def get_products_with_categories(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            products.id,
            products.name AS product_name,
            products.price,
            categories.name AS category_name
        FROM
            products
        JOIN
            categories ON products.category_id = categories.id
    ''')
    return cursor.fetchall()

if __name__ == '__main__':
    conn = sqlite3.connect('shop.db')

    create_tables(conn)

    categories_data = [
        ('Jeans',),
        ('T-Shirts',),
        ('Dresses',)
    ]

    products_data = [
        ("Blue Jeans", "Classic blue denim jeans", 799.00, 1),
        ("Ripped Jeans", "Trendy ripped style jeans", 899.00, 1),
        ("White T-Shirt", "Basic crew neck T-shirt", 299.00, 2),
        ("Black T-Shirt", "Printed cotton T-shirt", 349.00, 2),
        ("Summer Dress", "Lightweight dress for warm weather", 1199.00, 3),
        ("Cocktail Dress", "Elegant evening cocktail dress", 1799.00, 3)
    ]

    insert_data(conn,categories_data, products_data)

    results = get_products_with_categories(conn)
    for row in results:
        print(row)

    conn.close()