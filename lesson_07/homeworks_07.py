# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("task 01")

print("Multiplication table:")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("task 2")
def sum_numbers (a, b):
    return a + b
    
c = sum_numbers(5, 7)
print(f"Сума чисел дорівнює {c}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("task 3")
def average(numbers): 
    return sum(numbers) / len(numbers) 

# Перевірка функції
nums = [3, 5, 5, 7, 10, 15]
result = average(nums)

print(f"Середнє арифметичне списку {nums} дорівнює {result}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("task 4")

def reverse_string(s):
    return s[::-1]

text = "Прочитай цей рядок у зворотному порядку!"
reverse_text = reverse_string(text)

print(f"Оригінальний рядок: {text}")
print(f"Реверсований рядок: {reverse_text}")
    
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("task 5")

def longest_word(words):
    return max(words, key=len)

word_list = ["New York", "Los Angeles", "Kyiv", "Porto"]
print(f"Найдовше слово у списку: {longest_word(word_list)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("task 6")

def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("task 7")

def sum_of_digits(number):
    """
    Функція обчислює суму всіх цифр натурального числа.
    """
    return sum(int(digit) for digit in str(number))

user_input = int(input("Введіть натуральне число: "))
result = sum_of_digits(user_input)

print(f"Сума цифр числа {user_input}: {result}")

# task 8
print("task 8")

def check_dublicates(items):
    return len(items) > len(set(items))
"""функція перевіряє чи є в списку дублікати"""

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2, "time", "time", "sun"]

unique_set = set(big_list)
has_duplicates = check_dublicates(big_list)
print("Чи є дублікати в списку?", "Так" if has_duplicates else "Ні")

# task 9
print("task 9")

def calculate_remainder(dividend, divisor):
    """Функція знаходить остачу від ділення числа dividend на divisor."""
    return dividend % divisor

pairs = [(8019, 8), (9907, 9), (2789, 5), (7248, 6), (7128, 5), (19224, 9)]

for dividend, divisor in pairs:
    remainder = calculate_remainder(dividend, divisor)
    print(f"{dividend} % {divisor} = {remainder}")

# task 10
print("task 10")

def calculate_total_cost(order: list):
    """
    Функція обчислює загальну вартість замовлення.
    """
    total_cost = 0

    for item in order:
        name, quantity, price = item
        total_cost = total_cost + (quantity * price)
    return total_cost

order_list = [
    ("Піца велика", 4, 274),
    ("Піца середня", 2, 218),
    ("Сік", 4, 35),
    ("Торт", 1, 350),
    ("Вода", 3, 21)
]

total_price = calculate_total_cost(order_list)

print(f"Загальна вартість замовлення: {total_price} грн")