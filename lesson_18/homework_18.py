import logging

logging.basicConfig(filename='homework_18.log', 
                    level=logging.INFO, encoding="utf8", 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generator_of_factorial(number):
    """Generator that generates a sequence of factorials for numbers from 0 to n (inclusive)"""
    factorial = 1
    for i in range(number + 1):
        if i > 0:
            factorial = factorial * i
        logging.info(f"Factorial of number {i} = {factorial}")
        yield factorial

test_number = 6
print(f'Factorials of numbers in range 0-{test_number}:')
for factorial in generator_of_factorial(test_number):
    print(factorial)