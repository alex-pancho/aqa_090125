# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("\ntask 01")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    number = int(input("Введіть число для множення: "))
    # Complete the while loop condition.
    while multiplier <= number:
        result = int(number * multiplier)
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
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
print("\ntask 02")
def sum_two_elements(x, y):
    sum_operation= x + y
    return sum_operation

# Перевірка
print(sum_two_elements(2, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\ntask 03")
def arithmetic_mean_of_numb_list(numbers_list):
    arithmetic_mean = sum(numbers_list) / len(numbers_list)
    return(arithmetic_mean)

# Перевірка
print(arithmetic_mean_of_numb_list([10, 20, 30, 40]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\ntask 04")
def reverse_string(defined_string):
    make_reverse_string = list(reversed(defined_string))
    return ''.join(make_reverse_string)

# Перевірка
print(reverse_string("I live in Kyiv"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\ntask 05")
def longest_word_in_list(list_of_words):
    word = max(list_of_words, key = len)
    return(word)

# Перевірка
print(longest_word_in_list(("abc","defg","hijkl","mnopqrs")))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\ntask 06")
def find_substring(str1, str2):
    if str1.find(str2) == -1:
        return -1
    entry_index_second_line_into_first = str1.find(str2)
    return entry_index_second_line_into_first

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
# task 7
print("\ntask 07")
def change_key_value_in_dict(dict_for_change):
    """Creates a new dict in which values ​​and keys will be replaced by places"""
    new_dict_with_switched_key_value = {}
    for key, value in dict_for_change.items():
        new_dict_with_switched_key_value[value] = key
    return(new_dict_with_switched_key_value)
    
print(change_key_value_in_dict({'contry':'Ukraine', 'continent': 'Europe', 'size': 123}))

# task 8
print("\ntask 08")
def pay_for_month(duration_of_payment, monthly_pay):
    """Calculates the cost of the product according to the payment term and the monthly payment amount"""
    total_sum_for_product = duration_of_payment * monthly_pay
    return total_sum_for_product

print(pay_for_month(12, 1158))

# task 9
print("\ntask 09")
def word_in_text(some_text_str, word_str):
    """Finds how many times word appears in text"""
    times_word_appears_in_text = some_text_str.count(word_str)
    return(times_word_appears_in_text)

print(word_in_text("Google перекладач. Безкоштовний сервіс Google миттєво перекладає слова, фрази й веб-сторінки з української на понад 100 мов і навпаки.", "Google"))

# task 10
print("\ntask 10")
def find_arithmetic_mean(el_1, el_2, el_3, el_4, el_5):
    """Finds the arithmetic mean of the digits in list from 5 elements"""
    list_of_digits = el_1, el_2, el_3, el_4, el_5
    arithmetic_mean = sum(list_of_digits) / len(list_of_digits)
    return(arithmetic_mean)

print(find_arithmetic_mean(2, 3, 5, 9, 9))