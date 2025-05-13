from app.database import create_table, get_connection

def perform_operation(op, a, b):
    if op == 'add':
        res = a + b
    elif op == 'subtract':
        res = a - b
    elif op == 'multiply':
        res = a * b
    elif op == 'divide':
        if b == 0:
            raise ValueError('Division by zero')
        res = a / b
    else:
        raise ValueError('Unknown operation')
    save_result(op, a, b, res)
    return res

def save_result(operation, operand1, operand2, result):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''
                INSERT INTO calculations (operation, operand1, operand2, result)
                VALUES (%s, %s, %s, %s)
                ''',
                (operation, operand1, operand2, result)
            )
        conn.commit()

def get_all_results():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM calculations")
            return cur.fetchall()

if __name__ == '__main__':
    create_table()