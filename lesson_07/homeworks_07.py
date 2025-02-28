# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")
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
    return a + b
print("Сумма чисел = ",sum_numbers(1,1))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def sum_numbers(a,b):
    return int((a * b)/2)
print("Среднее арифметическое чисел = ",sum_numbers(21,2))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_string(text):
    return text[::-1]
result = revers_string("Напишите тут свой текст")
print("Строка наоборот = ",result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_list(words):
    return max(words, key=len)

word_list = ["apple", "banana", "strawberry", "kiwi"]
print(longest_word_list(word_list))
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

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

line = input("Введіть ваш текст:")
def count_unique_chars(line):
    unique_chars = len(set(line))
    return unique_chars > 10
print(count_unique_chars(line))

# task 8
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі, так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"

def word_with_h():
    while True:
        word = input("Введіть ваше слово з літерою 'h':")
        if "h" in word.lower():
            print(f"Дякую, слово '{word}' містить букву 'h'.")
            break
        else:
            print(f"На жаль слово '{word}' не містить букву 'h'. Спробуйте ще раз.")
word_with_h()

# task 9
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]
list_2= filter_strings(list_1)
print(list_2)

# task 10
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def sum_with_numbers(lst):
    sum = 0
    for number in lst:
        if isinstance(number, int) and number % 2 == 0:
            sum += number
    return sum
list_with_numbers = [1, 2, 45, 7, 56, 83, 29, 61, 34, 78, 15, 90, 64]
print(sum_with_numbers(list_with_numbers))