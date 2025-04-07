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

def create_tables():    # Створення таблиць
    conn = sqlite3.connect('online_store.db')
    cursor = conn.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)''')
    
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id))''')
    
    conn.commit()
    conn.close()

def insert_sample_data():    # Заповнення таблиць
    conn = sqlite3.connect('online_store.db')
    cursor = conn.cursor()
    
    categories = [
        ('Догляд за волоссям',),
        ('Догляд за обличчам',),
        ('Макіяж',)
    ]
    cursor.executemany('INSERT INTO categories (name) VALUES (?)', categories)
    
    products = [
        ('Шампунь', 'Шампунь для надання об\'єму волоссю', 1000, 1),
        ('Бальзам', 'Бальзам для надання волоссю блиску', 1800, 1),
        ('Маска', 'Маска для живлення волосся', 2200, 1),
        ('Тонік', 'Зволожувальний тонік для обличча', 1100, 2),
        ('Крем', 'Заспокійливий нічний крем для обличча', 2000, 2),
        ('Сироватка', 'Сироватка з вітаміном С', 1500, 2),
        ('Туш', 'Туш для подовження вій', 1900, 3),
        ('Пудра', 'Пудра з матовим фінішем', 1300, 3),
        ('Блиск для губ', 'Зволожувальний блиск для губ з гіалуроновою кислотою', 2100, 3)
    ]
    cursor.executemany('''INSERT INTO products (name, description, price, category_id) 
                          VALUES (?, ?, ?, ?)''', products)
    
    conn.commit()
    conn.close()

def get_products_with_categories():    # Отримання даних
    conn = sqlite3.connect('online_store.db')
    cursor = conn.cursor()
    
    
    cursor.execute('''SELECT p.id, p.name, p.description, p.price, c.name as category_name
                      FROM products p
                      LEFT JOIN categories c ON p.category_id = c.id''')
    
    products = cursor.fetchall()
    conn.close()
    
    return products


if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    
    
    print("Список продуктів з категоріями:")
    for product in get_products_with_categories():
        print(f"ID: {product[0]}, Назва: {product[1]}, Опис: {product[2]}, "
              f"Ціна: {product[3]:.2f} грн, Категорія: {product[4]}")