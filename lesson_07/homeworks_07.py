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
def sum_of_two_numbers(a, b):
    """Sum of two numbers a and b"""
    return  a + b

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    """Calculates the arithmetic mean of a list of numbers"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    """Returns string in reverse order"""
    return s[::-1]
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    """Finding longest word"""
    if not words:
        return None

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

word_list = ["apple", "banana", "strawberry", "kiwi"]
print(longest_word(word_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """Finding the index of the first entry of another row in the first row """
    return str1.find(str2)

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
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# from homework 5 task 8
def unique_elements_sum(set_1, set_2):
    """Finding unique elements from two multiplier values and summary them"""
    set_3 = set_1 ^ set_2
    return sum(set_3)

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
result = unique_elements_sum(set_1, set_2)

print("Сума елементів двох множин, які не є спільними:", result)

#homework 6 task 5
def choose_pizza_toppings():
    """ The function adding pizza toppings to the list and showing it to customer"""
    pizza_toppings = []

    while True:
        topping_name = input("Введіть назву начинки, або напишіть 'quit' для завершення: ")
        if topping_name.lower() == 'quit':
            break
        else:
            pizza_toppings.append(topping_name)
            print(f"Ми додали {topping_name} до вашої піци")

    print("\nЗагалом ви додали такі начинки:")
    for topping in pizza_toppings:
        print(f"- {topping}")

choose_pizza_toppings()

#homework 6 task 6
def sum_of_digits(number):
    """The function calculates the sum of digits of a natural number."""
    sum_digits = sum(int(digit) for digit in str(number))
    return sum_digits

number = input("Введіть натуральне число: ")
print(f"Сума цифр числа {number}: {sum_of_digits(number)}")

#homework 6 task 7
def sum_user_numbers():
    """The function sums the numbers entered by the user until 0 is entered."""
    sum_calculation = 0

    while True:
        number_from_user = int(input("Введіть число (0 для завершення): "))
        if number_from_user == 0:
            break
        sum_calculation += number_from_user
        print(f"Поточна сума: {sum_calculation}")

    print(f"Загальна сума введених чисел: {sum_calculation}")

sum_user_numbers()

