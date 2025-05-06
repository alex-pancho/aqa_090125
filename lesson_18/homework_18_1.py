import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("factorial.log"),
        logging.StreamHandler()
    ]
)

def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_generator(n):
    """Генерує факторіали чисел від 0 до n включно з логуванням."""
    for i in range(n + 1):
        logging.info(f"Calling factorial({i})")
        result = factorial(i)
        logging.info(f"Result: {result}")
        yield result

if __name__ == "__main__":
    for f in factorial_generator(5):
        pass        