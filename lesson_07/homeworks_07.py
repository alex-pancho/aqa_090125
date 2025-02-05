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
        if result > 25:
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


def two_numbers_sum(first_number: int, second_number: int) -> int:
    return first_number + second_number


print(two_numbers_sum(1, 2))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def verify_arithmetic_mean(*args):
    return sum(args) / len(args)  # it is example with tuple


print(verify_arithmetic_mean(1, 2, 3))


# second variant


def verify_arithmetic_mean_of_list(number_list: list = None):
    return sum(number_list) / len(number_list)


print(verify_arithmetic_mean_of_list([1, 2, 3]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_list(_list: list = None) -> list:
    _list.reverse()
    return _list


print(reverse_list([1, 2, 3]))


def reverse_list_second_variant(_list: list = None) -> list:
    return _list[::-1]


print(reverse_list_second_variant([1, 2, 3]))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def get_longest_word(word_list: list[str] = None) -> str:
    return max(word_list, key=len)


print(get_longest_word(["Hello", "people"]))


# second variant
def find_longest_words(words: list[str] = None) -> str:
    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length][0]


print(find_longest_words(["Hello", "people"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""


def natural_numbers_sum(number: int) -> int:
    return sum(map(int, str(number)))  # also can use this one: sum([int(i) for i in str(number)]


print(natural_numbers_sum(12345))


"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""


def squares_paired_numbers(numbers: list[int]) -> list:
    return [i ** 2 for i in numbers if i % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(squares_paired_numbers(numbers))


# task 8. Обчисліть суму елементів двох множин, які не є спільними

def sum_unique_numbers(set_1: set, set_2: set) -> set:
    return sum(set_1^set_2)

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

print(sum_unique_numbers(set_1, set_2))


# task 3. Перевірте, чи є в списку big_list дублікати

def verify_duplicates(big_list: list[int]) -> bool:
    return len(set(big_list)) < len(big_list)


big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
print(verify_duplicates(big_list))
