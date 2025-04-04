import sqlite3
from pathlib import Path


class DatabaseClass:
    """ Container for database connection with all necessary methods """
    def __init__(self, database_name: str):
        """ Constructor for database connection """
        self.db = Path(__file__).resolve().parent / database_name

        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()

            query = """
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category_name VARCHAR(50) NOT NULL
                )
            """

            cursor.execute(query)

            query = """
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name VARCHAR(50) NOT NULL,
                    product_description TEXT NOT NULL,
                    product_price DECIMAL(10, 2) NOT NULL,
                    product_category_id INTEGER DEFAULT NULL,
                    FOREIGN KEY(product_category_id) REFERENCES categories(id)
                )
            """

            cursor.execute(query)
            connection.commit()

    def get_products_by_category_id(self, cat_id: int):
        """ Get all products by 'category id' """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()

            query = """ 
                SELECT products.product_name, products.product_description, products.product_price, categories.category_name 
                FROM products
                INNER JOIN categories ON products.product_category_id = categories.id
                WHERE products.product_category_id LIKE :cat_id
            """

            result = cursor.execute(query, {"cat_id": cat_id}).fetchall()
            return result

    def add_product(self, *, product_data: tuple):
        """ Add product with automatically assigned ID. 'product_data' tuple must contain 4 values. """
        name, description, price, category_id = product_data
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            values = [name, description, price, category_id]

            query = """ 
                INSERT INTO products (product_name, product_description, product_price, product_category_id)
                VALUES (?, ?, ?, ?)
            """

            cursor.execute(query, values)
            connection.commit()

    def add_category(self, *, category_name: str):
        """ Add new category. Category ID assigned automatically """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            values = [category_name]
            query = """ 
                INSERT INTO categories (category_name) VALUES (?)
            """
            cursor.execute(query, values)
            connection.commit()

    def get_all_categories(self):
        """ Get all categories """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()

            query = """
                SELECT category_name FROM categories
            """
            cursor.execute(query)
            categories = cursor.fetchall()
            return categories

    def get_all_products(self):
        """ Get all products, including with no category assigned. """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()

            query = """ 
                SELECT products.product_name, products.product_description, products.product_price, categories.category_name 
                FROM products
                LEFT JOIN categories ON products.product_category_id = categories.id
            """

            result = cursor.execute(query).fetchall()
            return result


database = DatabaseClass('lesson_20.sqlite3')
