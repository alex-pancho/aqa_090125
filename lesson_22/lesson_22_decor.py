def outer(x):
    def inner(y):
        return x + y
    return inner

# add_five = outer(5) # 
# print(add_five)
# result = add_five(6)
# result = outer(5)(6)
# print(result)

def add(x, y):
    return x + y

def diff(x, y):
    return x - y

def calculate(func, x, y):
    return func(x, y)
 
# result_a = calculate(add, 4, 6)
# result_b = calculate(diff, 4, 6)
# print(result_a, result_b)

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello
 
# greet = greeting("Atlantis")
# print(greet())

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if isinstance(args[0],int):
            print("I like numbers")
        else:
            print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

@my_decorator
def a_plus_b(a, b):
    print(a+b)

say_hello("Kseniya")

a_plus_b(1,2)
