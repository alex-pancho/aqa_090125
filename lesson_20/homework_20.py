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


def create_table(cursor, create_table_query):
    cursor.execute(create_table_query)

def insert_data(cursor, insert_query, insert_data):
    cursor.executemany(insert_query, insert_data)

def get_products_with_categories(cursor, join_query):
    cursor.execute(join_query)
    return cursor.fetchall()


if __name__ == '__main__':

    conn = sqlite3.connect('online_shop.db')
    cursor = conn.cursor()

    create_categories_table_query = '''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT
        )
        '''

    create_products_table_query = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            description TEXT,
            price REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
        '''

    insert_categories_query = 'INSERT INTO categories (category_name) VALUES (?)'
    insert_products_query = 'INSERT INTO products (product_name, description, price, category_id) VALUES (?, ?, ?, ?)'

    categories_data = [('Electronics',), ('Clothing',), ('Books',)]
    products_data = [
        ('Smartphone', 'Modern smartphone with a large screen', 999.99, 1),
        ('T-shirt', 'Cotton t-shirt in various colors', 29.99, 2),
        ('Book "The Lord of the Rings"', 'Fantasy novel by J. R. R. Tolkien', 19.95, 3),
        ('Laptop', 'Powerful laptop for work and games', 1499.00, 1),
        ('Jeans', 'Classic denim jeans', 49.99, 2)
    ]

    join_query = '''
        SELECT products.product_name, products.description, products.price, categories.category_name
        FROM products
        JOIN categories ON products.category_id = categories.category_id
    '''

    create_table(cursor, create_categories_table_query)
    create_table(cursor, create_products_table_query)
    
    insert_data(cursor, insert_categories_query, categories_data)
    insert_data(cursor, insert_products_query, products_data)

    products_with_categories = get_products_with_categories(cursor, join_query)

    for product in products_with_categories:
        print(f'Name: {product[0]}, Description: {product[1]}, Price: {product[2]}, Category: {product[3]}')

    conn.commit()
    conn.close()