import psycopg2
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def db_cursor(commit=True):
    conn = psycopg2.connect(
        dbname="math_db",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def init_db():
    with db_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id SERIAL PRIMARY KEY,
                operation TEXT,
                a INT,
                b INT,
                result FLOAT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

def insert_result(operation, a, b, result):
    with db_cursor() as cursor:
        cursor.execute("INSERT INTO results (operation, a, b, result, created_at) VALUES (%s, %s, %s, %s, %s)",
                       (operation, a, b, result, datetime.now()))
        
def update_result(operation, new_result):
    with db_cursor() as cursor:
        cursor.execute("UPDATE results SET result = %s WHERE operation = %s",
                       (new_result, operation))
        
def fetch_results():
    with db_cursor() as cursor:
        cursor.execute("SELECT * FROM results")
        rows = cursor.fetchall()
    return rows

def delete_result(operation):
    with db_cursor() as cursor:
        cursor.execute("DELETE FROM results WHERE operation = %s", (operation,))
    