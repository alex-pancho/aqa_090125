from db import init_db, insert_result, get_results

def main():
    init_db()
    a, b = 5, 3
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b,
    }

    for op, result in operations.items():
        insert_result(op, result)

    for row in get_results():
        print(row)

