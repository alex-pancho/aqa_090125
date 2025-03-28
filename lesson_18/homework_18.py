import pytest

from lesson_18.logger import logger


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__}({args[0]})")
        result = func(*args, **kwargs)
        logger.info(f"Result: {result}")
        return result

    return wrapper


@log_decorator
def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)


class ReverseList:
    """ ітератор для зворотного виведення елементів списку"""
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.index = len(numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        index = self.index
        self.index -= 1
        return self.numbers[index]

    def __setattr__(self, name, value):
        if name == 'numbers':
            if not isinstance(value, list):
                raise TypeError(f"Expected a list, got {type(value)}")

        super().__setattr__(name, value)


def exception_decorator(msg):
    def catch_exception(func):
        def wrapper(*args, **kwargs):
            with pytest.raises(TypeError) as e:
                logger.info(f"Input value: {args[0]}")
                func(*args, **kwargs)
            logger.info(e)
            assert e.value.args[0] == msg, f"Expected msg={msg}, got actual = {e.value.args[0]}"
        return wrapper
    return catch_exception


@exception_decorator("Expected a list, got <class 'int'>")
def check_exception_decorator(number):
    ReverseList(number)


class EvenNumbers:
    """Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration

        current = self.current
        self.current += 2
        return current


def even_generator(number):
    for i in range(number):
        if i % 2 == 0:
            yield i


def even_number_generator(n):
    current = 0
    while current <= n:
        yield current
        current += 2


def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    res = factorial_generator(5)
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))

    for i in factorial_generator(5):
        print(i)

    res = ReverseList([1, 2, 3, 4, 5])
    for i in res:
        print(i)

    even_numbers = EvenNumbers(11)
    for i in even_numbers:
        print(i)

    for i in even_generator(5):
        print(i)

    for number in even_number_generator(10):
        print(number)

    for number in fibonacci_generator(20):
        print(number)

    print(check_exception_decorator(5))
