import logging


def factorial(n):
    if n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел")
    result = 1 
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(n):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')
    
    for i in range(n + 1):
        result = factorial(i)
        logging.info(f"Факторіал {i}! = {result}")
        yield result

if __name__ == '__main__':
    print("Обчислення факторіалів:")
    for value in factorial_generator(5):
        pass 