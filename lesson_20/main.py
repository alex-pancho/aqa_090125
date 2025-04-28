from db import create_connection, close_connection
from schema import create_tables
from seeder import insert_initial_data
from queries import get_products_with_categories
from random_data import generate_random_categories, generate_random_products

import logging

# Налаштування логера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    database = "store.db"
    logging.info(f"Attempting to connect to database: {database}")
    conn = create_connection(database)

    if conn:
        logging.info("Connection established successfully.")

        # Створюємо таблиці
        logging.info("Creating tables...")
        create_tables(conn)
        
        # Вставка початкових даних
        logging.info("Inserting initial data into the database...")
        insert_initial_data(conn)

        # Отримуємо і виводимо на екран продукти з категоріями
        logging.info("Fetching products with their categories...")
        products = get_products_with_categories(conn)
        for p in products:
            logging.info(f"Product: {p[0]}, Description: {p[1]}, Price: {p[2]}, Category: {p[3]}")

        # Вставка випадкових категорій
        logging.info("Generating and inserting random categories...")
        random_categories = generate_random_categories(5)
        logging.info(f"Inserting the following random categories: {random_categories}")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO categories (name) VALUES (?)", random_categories)
        conn.commit()
        logging.info(f"{len(random_categories)} random categories inserted.")

        # Отримуємо оновлені id категорій
        logging.info("Fetching category IDs from the database...")
        cursor.execute("SELECT id FROM categories")
        category_ids = [row[0] for row in cursor.fetchall()]

        # Вставка випадкових продуктів
        logging.info("Generating and inserting random products...")
        random_products = generate_random_products(10, category_ids)
        logging.info(f"Inserting the following random products: {random_products}")
        cursor.executemany("INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)", random_products)
        conn.commit()
        logging.info(f"{len(random_products)} random products inserted.")

        # Ще раз виводимо усі продукти з категоріями
        logging.info("Fetching and displaying all products with their categories after insertion...")
        products = get_products_with_categories(conn)
        for p in products:
            logging.info(f"Product: {p[0]}, Description: {p[1]}, Price: {p[2]}, Category: {p[3]}")

        # Закриваємо з'єднання
        logging.info("Closing database connection...")
        close_connection(conn)

    else:
        logging.error("Failed to create database connection")


if __name__ == "__main__":
    main()
