import sqlite3

def get_products_with_categories(conn):
    """Get products with their corresponding category names."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT products.name, products.description, products.price, categories.name AS category_name
            FROM products
            JOIN categories ON products.category_id = categories.id
        """)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
