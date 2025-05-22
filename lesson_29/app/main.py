from app.db import init_db, insert_result
from app.operations import add, substract, multiply, divide

if __name__ == "__main__":
    init_db()

    result1 = add(5, 3)
    insert_result("add", 5, 3, result1)

    result2 = substract(10, 4)
    insert_result("substract", 10, 4, result2)

    result3 = multiply(6, 7)
    insert_result("multiply", 6, 7, result3)

    result4 = divide(8, 2)
    insert_result("divide", 8, 2, result4)

    print("All operations completed and results added to DB.")