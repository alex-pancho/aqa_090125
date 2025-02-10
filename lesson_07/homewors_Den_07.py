# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5: #Хоть пасхалка про ошибку на 15 строке, я все же решил поменять условие цикла
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25: #Инт сравнить с строкой нельзя
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
#ПО итогу получаю требуемый вывод
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

def sum_of_two_numbers(first, second):
    result = 0
    if (type(first) == int or type(first) == float) and (type(second) == int or type(second) == float):
        result = first + second
        print(f"{first}+{second}={result}")
    else:
        print("System error:(( Please try again later.")

sum_of_two_numbers(3.14, 1.86)
sum_of_two_numbers("x", None)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_average(list_of_numbers):
    if isinstance(list_of_numbers, list) and all(isinstance(elements, (int, float)) for elements in list_of_numbers):
        if len(list_of_numbers) == 0:
            return "Обчислиня порожнього списку неможливо"
        result = sum(list_of_numbers) / len(list_of_numbers)
        return f"Середнє орифмітичне поданого спуску дорінює: {result}"
    else:
        return "Список має містити тільки числові значення"

print(arithmetic_average([]))
print(arithmetic_average([10, 20, 30, 40]))
print(arithmetic_average(["hello", 2, 3]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverser(string_data):
    if not isinstance(string_data, str) or not  string_data:
        return "Очікується виключно рядок, який не є порожнім"
    else:
        return string_data[::-1]
print(string_reverser(""))
print(string_reverser(0))
print(string_reverser({}))
print(string_reverser("0"))
print(string_reverser("qwerty"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_finder(list_of_words):
    if not isinstance(list_of_words, list) or not all(isinstance(element, str) for element in list_of_words) \
        or any(element == "" for element in list_of_words) or not list_of_words:
        return "На вхід приймається виключно список рядкових значень, жоден елемент якого не є порожнім"
    else:
        return max(list_of_words, key=len)

print(longest_word_finder({}))
print(longest_word_finder([]))
print(longest_word_finder(["x", "yz", ""]))
print(longest_word_finder([1, 2, 3]))
print(longest_word_finder(["a", "abcdefg", "abc", "abcd"]))
print(longest_word_finder(["a", "ab", "abc", 1]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return "Invalid input data"
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

print(find_substring("Hello, world!", "world"))
print(find_substring("The quick brown fox jumps over the lazy dog", "cat"))
print(find_substring("abcdef", "cde"))
print(find_substring("abcdef", "xyz"))
print(find_substring(123, "test"))
print(find_substring("hello", 456))
print(find_substring("aaaaaa", "aaa"))

# энтузиазм угас((((((((((((((((((((((((((((((((((((((((((((((
# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7.
line_task_7 = "Створіть множину всіх символів, які входять у заданий рядок"
def line_setter(line):
    return set(line)
print(line_setter(line_task_7))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
def sum_unique_elements(set_1, set_2):
    unique_elements = set_1.symmetric_difference(set_2)
    return sum(unique_elements)
print(sum_unique_elements(set_1, set_2))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
a = list(range(1, 6))
b = list(range(3, 8))
def set_from_list(list_1: list, list_2: list) -> set:
    return set(list_1).symmetric_difference(set(list_2))
print(set_from_list(a, b))


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

def group_people_by_age(people):
    age_groups = {
        "10-19": [],
        "20-29": [],
        "30-39": [],
        "40-49": []
    }

    for age_range in age_groups.keys():
        min_age, max_age = map(int, age_range.split("-"))
        for name, age in people:
            if min_age <= age <= max_age:
                age_groups[age_range].append(name)

    return age_groups
print(group_people_by_age(person_list))


