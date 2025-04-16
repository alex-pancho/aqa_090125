def log_function_call(func):
    def wrapper(n):
        print(f"Calling {func.__name__}({n})")
        result = func(n)
        print(f"Result: {result}")
        return result
    return wrapper


@log_function_call
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(limit):
    for i in range(limit + 1):
        yield factorial(i)


if __name__ == "__main__":
    for value in factorial_generator(5):
        pass
