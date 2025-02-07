# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break

        print(f"{number} x {multiplier} = {result}")
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10))  # 15

# task 3
def average(numbers):
    summ = sum(numbers)
    number_qty = len(numbers)
    if len(numbers) == 0:
        print('Ми не ділимо на 0 в цьому коді')
    else:
        average = summ/ number_qty
    return average
print(average([10, 20, 30]))

# task 4
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# task 5
def longest_word(words):
    """Повертає найдовше слово зі списку."""
    return max(words, key=len) if words else ""

print(longest_word(["apple", "bananar", "cherryyy"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

print(find_substring("Hello, world!", "world"))  # 7
print(find_substring("The quick brown fox", "cat"))

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

def contains_h():
    while True:
        word = input("Введіть слово з буквою 'h': ")
        if 'h' in word.lower():
            return "Дякую! Ви ввели правильне слово."

print(contains_h())

def squares_of_even(numbers):
    return [num ** 2 for num in numbers if num % 2 == 0]

print(squares_of_even([1, 2, 3, 4, 5, 6]))
#Підраховує суму введених чисел, доки не буде введено 0
def sum_until_zero():
    total = 0
    while True:
        num = int(input("Введіть число (0 для завершення): "))
        if num == 0:
            return total
        total += num

print(sum_until_zero())

def print_fruits_without_orange(fruit_list):
    for fruit in fruit_list:
        if fruit == "orange":
            continue
        print(fruit)


fruits = ["apple", "banana", "orange", "grape", "mango"]
print(print_fruits_without_orange(fruits))