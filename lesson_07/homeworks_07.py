# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
from operator import truth

print("\n", "task 1")
def multiplication_table(number):
    """функція, яка надрукує табличку множення на задане число, але лише до максимального значення для добутку - 25"""
    multiplier = 1
    while multiplier <= 10:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
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
print("\n", "task 2")
def summ_of_two_numbers(a, b):
    """функція, яка обчислює суму двох чисел."""
    return a + b

print(summ_of_two_numbers(3,5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\n", "task 3")
def arithmetic_mean(numbers):
    """функція, яка розрахує середнє арифметичне списку чисел."""
    return  sum(numbers) / len(numbers)

print(arithmetic_mean([2,3,4,5,6]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\n", "task 4")
def reverse_string(sentence):
    """функція, яка приймає рядок та повертає його у зворотному порядку."""
    return sentence[::-1]

print(reverse_string("функція, яка приймає рядок та повертає його у зворотному порядку."))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\n", "task 5")
def longest_string(sentence):
    """функція, яка приймає список слів та повертає найдовше слово у списку."""
    return sorted(sentence, key=len)[-1]

print(longest_string(['Написати', 'функцію', 'яка', 'приймає', 'список', 'слів']))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\n", "task 6")
def find_substring(value1, value2):
    """функція, яка приймає два рядки та повертає індекс першого входження другого рядка у перший рядок.
    якщо другий рядок не є підрядком першого рядка повертає -1 """
    if value2 in value1:
        return tuple(value1).index(tuple(value2)[0])
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
print("\n", "task 7")
def alien_color(set_1, set_2):
    """функція, яка обчислює суму елементів двох множин, які не є спільними"""
    return sum(set_1.symmetric_difference(set_2))

print(alien_color({1, 2, 3, 4, 5}, {4, 6, 5, 10}))

print("\n", "task 8")
def find_duplicates(list_of_values):
    """ функція, яка перевіряє чи є в списку дублікати """
    return len(list_of_values) != len(set(list_of_values))

print(find_duplicates([3, 5, -2, -1, -3, 0, 1, 4, 5, 2]))

print("\n", "task 9")
def count_a(sentence):
    """ функція, яка порахує скільки разів зустрічається літера а """
    return sentence.count("а")

print(count_a("Оберіть будь-які 4 таски з попередніх домашніх робіт та перетворіть їх у 4 функції, що отримують значення та повертають результат."))

print("\n", "task 10")
def summ_of_number_items(number):
    """функція, яка знаходить суму всіх цифр натурального числа, яке вводить користувач"""
    counter = []
    for i in number:
        counter.append(i)
    return sum([int (i) for i in counter])

print(summ_of_number_items(input("Введіть натуральне число: ")))

