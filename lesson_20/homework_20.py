import sqlite3
from sqlite3 import Error
import random
import string
import logging
from datetime import datetime, timedelta

# Налаштовуємо логер
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Функція для створення з'єднання з базою даних
def create_connection(db_file):
    """ створює з'єднання з SQLite базою даних """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except Error as e:
        logging.error(f"Error connecting to database: {e}")
    return conn


# Функція для закриття з'єднання з базою даних
def close_connection(conn):
    """ закриває з'єднання з SQLite базою даних """
    if conn:
        conn.close()
        logging.info("Connection closed")


# Функція для створення таблиць
def create_tables(conn):
    """ створює таблиці products та categories """
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
        logging.info("Tables created successfully")
    except Error as e:
        logging.error(f"Error creating tables: {e}")


# Функція для вставки даних у таблиці
def insert_data(conn):
    """ вставляє дані у таблиці products та categories """
    try:
        cursor = conn.cursor()

        # Перевірка, чи є вже категорії та продукти
        cursor.execute("SELECT COUNT(*) FROM categories")
        category_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM products")
        product_count = cursor.fetchone()[0]

        if category_count == 0:
            categories = [
                ('Electronics',),
                ('Clothing',),
                ('Books',),
                ('Home & Kitchen',),
                ('Sports',)
            ]
            cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

        if product_count == 0:
            products = [
                ('Smartphone', 'Latest model smartphone with advanced features.', 699.99, 1),
                ('T-shirt', 'Comfortable cotton t-shirt.', 19.99, 2),
                ('Novel', 'Bestselling novel of the year.', 14.99, 3),
                ('Blender', 'High-speed blender for smoothies and soups.', 49.99, 4),
                ('Soccer Ball', 'Official size soccer ball for training.', 29.99, 5)
            ]
            cursor.executemany("INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)", products)

        conn.commit()
        logging.info("Data inserted successfully")
    except Error as e:
        logging.error(f"Error inserting data: {e}")


# Функція для виконання JOIN-запиту
def join_query(conn):
    """ виконує JOIN-запит для отримання інформації про продукти та їх категорії """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT products.name, products.description, products.price, categories.name AS category_name
            FROM products
            JOIN categories ON products.category_id = categories.id
        """)
        rows = cursor.fetchall()
        for row in rows:
            logging.info(f"Product: {row[0]}, Description: {row[1]}, Price: {row[2]}, Category: {row[3]}")
    except Error as e:
        logging.error(f"Error executing join query: {e}")


# Функція для генерації випадкових даних
def random_string(length=10):
    """ Генерує випадковий рядок заданої довжини """
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def random_price(min_price=1.0, max_price=1000.0):
    """ Генерує випадкову ціну в заданому діапазоні """
    return round(random.uniform(min_price, max_price), 2)


def random_date(start_date, end_date):
    """ Генерує випадкову дату в заданому діапазоні """
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_random_data(num_products=10, num_categories=5):
    """ Генерує випадкові дані для продуктів та категорій """
    categories = [(random_string(10),) for _ in range(num_categories)]
    products = [
        (random_string(10), random_string(20), random_price(), random.randint(1, num_categories))
        for _ in range(num_products)
    ]
    return categories, products


# Головна функція
def main():
    database = "store.db"

    # Створюємо з'єднання з базою даних
    conn = create_connection(database)

    # Створюємо таблиці
    if conn:
        create_tables(conn)

        # Вставляємо дані
        insert_data(conn)

        # Виконуємо JOIN-запит
        join_query(conn)

        # Генерація випадкових даних
        categories, products = generate_random_data()
        logging.info(f"Generated categories: {categories}")
        logging.info(f"Generated products: {products}")

        # Вставка випадкових даних у базу даних
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
        cursor.executemany("INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)", products)
        conn.commit()
        logging.info("Random data inserted successfully")

        # Виконання JOIN-запиту з випадковими даними
        join_query(conn)

        # Закриваємо з'єднання
        close_connection(conn)
    else:
        logging.error("Failed to create database connection")


if __name__ == '__main__':
    main()
