import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname='mathdb',
        user='postgres',
        password='postgres',
        host='db',
        port=5432
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id SERIAL PRIMARY KEY,
        operation TEXT NOT NULL,
        result FLOAT NOT NULL
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_result(operation, result):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO results (operation, result) VALUES (%s, %s)", (operation, result))
    conn.commit()
    cur.close()
    conn.close()

def get_results():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM results")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_result(result_id, new_result):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE results SET result = %s WHERE id = %s", (new_result, result_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_result(result_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM results WHERE id = %s", (result_id,))
    conn.commit()
    cur.close()
    conn.close()

