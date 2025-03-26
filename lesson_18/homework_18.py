import logging

def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_generator(n):
    #Logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    for i in range(n + 1):
        result = factorial(i)
        logging.info(f"Факторіал від {i}! = {result}")
        yield result


if __name__ == '__main__':
    factorials = factorial_generator(5)
    for fact in factorials:
        pass
