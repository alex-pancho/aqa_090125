# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
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
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

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

def sum_numbers(a,b):
    result = a + b
    return(f"a + b = {result}")

print(sum_numbers(5,6))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [1,2,3,4,5]

def average(numbers):
    return sum(numbers) / len(numbers) 

print(average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(s):
    return s[::-1]

print(reverse_string("coffe"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    return max(words, key=len)

print(longest_word(["la", "lala", "lalalala"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
"""Знайдіть всі унікальні елементи в списку small_list"""

def unique_elements(lst):
    return list(set(lst))

print(unique_elements(small_list))

# task 8
"""Перевірте, чи є в списку big_list дублікати"""
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates(big_list))

# task 9
"""Обчисліть суму елементів двох множин, які не є спільними"""
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

def sum_unique_elements(set1, set2):
    return sum(set1 ^ set2)

print(sum_unique_elements(set_1, set_2))

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
