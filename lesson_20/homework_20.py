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

conn = sqlite3.connect('homework_20.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
''')

cursor.executemany('INSERT INTO categories (name) VALUES (?)', 
[
    ("Bakery",),
    ("Meat",),
    ("Drinks",),
    ("Home goods",)
])

cursor.executemany('INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)', [
    ("Cinnamon roll", "Sweet baked dough filled with a cinnamon-sugar filling", 50, 1),
    ("Beefstake", "Cut of beef with parallel faces, usually cut perpendicular to the muscle fibers", 500, 2),
    ("Pepsi twist", "Lemon flavoured cola", 25, 3),
    ("Capuccino cup", "Capuccino cup made of high quality porcelain", 150, 4)
])

cursor.execute('''
SELECT products.name AS product_name, products.description, products.price, categories.name AS category_name
FROM products
JOIN categories ON products.category_id = categories.id
''')

result = cursor.fetchall()

def print_result(rows):
    for row in rows:
        print(f'Product: {row[0]}, Description: {row[1]}, Price: {row[2]}, Category: {row[3]}')

print_result(result)

conn.close()