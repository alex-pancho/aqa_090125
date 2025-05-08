import psycopg2

conn = psycopg2.connect(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
# create_table = """
# CREATE TABLE IF NOT EXISTS test_table (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INT
# );
# """
# cur.execute(create_table)
# conn.commit()
# insert = """INSERT INTO test_table (name, age) VALUES ('Alice', 35), ('Bob', 40);"""
# cur.execute(insert)
# conn.commit()
cur.execute("SELECT * FROM test_table")
rows = cur.fetchall()
print(rows)