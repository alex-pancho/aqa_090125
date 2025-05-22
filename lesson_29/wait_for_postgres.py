import time
import psycopg2
from psycopg2 import OperationalError

for i in range(30):
    try:
        conn = psycopg2.connect(
            dbname="math_db",
            user="postgres",
            password="postgres",
            host="db",
            port="5432"
        )
        conn.close()
        print("Database is ready!")
        break
    except OperationalError:
        print("Waiting for database...")
        time.sleep(1)
else:
    raise Exception("Database not available after 30 seconds")