import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    'host': 'localhost',  # назва сервісу в docker-compose
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS calculations (
                    id SERIAL PRIMARY KEY,
                    operation VARCHAR(10),
                    operand1 FLOAT,
                    operand2 FLOAT,
                    result FLOAT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
        conn.commit()