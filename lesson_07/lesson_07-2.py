def describe_pet(animal_type:str, pet_name:str):
    """Display information about a pet."""
    return f"My {animal_type}'s name is {pet_name.title()}."

my_pet = describe_pet("cat", "Sam")
print(my_pet)

def describe_pet(animal_type:str="cat", pet_name:str="Cat"):
    """Display information about a pet."""
    return f"My {animal_type}'s name is {pet_name.title()}."

my_pet = describe_pet(pet_name="Basya", animal_type="cat")
print(my_pet)
my_pet = describe_pet("dog", "Jack")
print(my_pet)

def print_args(*katya):
    for arg in katya:
        print(arg)
print_args(1, "hello", 3.14, [1, 2, 3], (1, 3, 5))
print_args("hello")

def print_kwargs(**kwargs):
    print(kwargs["name"])
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_kwargs(name="John", age=25, city="New York")

def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_args_and_kwargs(1, "hello", 3.14, name="John", age=25)
print(print())

# lambda arguments: expression

square = lambda x, y: x*y
sum_ = lambda x, y: x+y
print(square(5,5))
print(sum_(5,5))
