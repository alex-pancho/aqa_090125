import sqlite3

# Підключення до бази даних (створює файл БД, якщо він не існує)
conn = sqlite3.connect('example.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS access (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date_time TEXT
    )
''')

# Збереження змін у базі даних
conn.commit()

# Оновлення даних
# cursor.execute('''
#     UPDATE users SET email = ? WHERE username = ?
# ''', ('john.doe@example.com', 'JohnDoe'))

# Збереження змін у базі даних
conn.commit()

# Вставка даних
cursor.execute('''
    INSERT INTO users (username, email) VALUES (?, ?)
''', ('Frlll', 'loo@example.com'))
# Збереження змін у базі даних
conn.commit()

def insert_access_info(cursor, user_id, date_time):
    cursor.execute('''
        INSERT INTO access (user_id, date_time) VALUES (?, ?)
    ''', (user_id, date_time))

    # Збереження змін у базі даних
    conn.commit()

userlog = [
    (3, "20250403T124546.7456784"),
    (3, "20250403T124547.7456784"),
    (3, "20250403T125547.7456784"),
    (4, "20250403T124546.7456784"),
    (1, "20250403T124546.7456784"),
    (2, "20250403T125547.7456784"),
    (5, "20250403T125547.7456784"),
]
# for val in userlog:
#     user_id, date_time = val
#     insert_access_info(cursor, user_id, date_time)
# Вибірка даних
select_cmd = 'SELECT * FROM users'
cursor.execute(select_cmd)

def query_output(cursor, select_cmd:str):
    rows = cursor.fetchall()
    print(f"Довжина вибірки команди: {select_cmd}: {len(rows)}")
    for row in rows:
        print(row)

query_output(cursor, select_cmd)

# # Видалення даних
# cursor.execute('DELETE FROM users WHERE username = ?', ('JohnDoe',))

# Збереження змін у базі даних
conn.commit()

# Вибірка даних
cursor.execute(select_cmd)
query_output(cursor, select_cmd)

select_cmd = "SELECT username, email, date_time, user_id FROM access RIGHT JOIN users ON access.user_id = users.id;"
# inner JOIN  a=a
# left       a = NONE
# Rigt      NONE = a
cursor.execute(select_cmd)
query_output(cursor, select_cmd)
# Закриття підключення
conn.close()
