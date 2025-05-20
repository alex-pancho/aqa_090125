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
    return res

if __name__ == '__main__':
    result = perform_operation("add", 2, 2)
    print(f"Результат: {result}")