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
def continuation_numbers(number_1,number_2):
    return number_1 + number_2

print(f"Total of '{number_1}' and '{number_2}'=",continuation_numbers ())

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(numbers_list):
    numbers_total= 0
    for numbers in numbers_list:
        numbers_total += numbers 
    arithmetic_mean_list = numbers_total / len(numbers_list)
    return arithmetic_mean_list

print("Arithmetic mean for number from list :", arithmetic_mean())

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_string(input_string):
    return input_string[::-1]

result = reversed_string(some_string_value)
print(f"Reversed string will be {result}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    longest = words
    for word in words_list[0:]:
        if len(word) > len(longest):
            longest = word 
    return longest

result = longest_word(words_list)
print(f"Longest word from list is: {result}")

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
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def continuation_numbers(number_1,number_2):
    return number_1 + number_2

number_1 = 10
number_2 = 500
print(f"Total of '{number_1}' and '{number_2}'=",continuation_numbers (number_1,number_2))

# task 8
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers_list = [2,3,5,10]

def arithmetic_mean(numbers_list):
    numbers_total= 0
    for numbers in numbers_list:
        numbers_total += numbers 
    arithmetic_mean_list = numbers_total / len(numbers_list)
    return arithmetic_mean_list

print("Arithmetic mean for number from list :", arithmetic_mean(numbers_list))

# task 9
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_string(input_string):
    return input_string[::-1]

result = reversed_string("hello")
print(f"Reversed string will be {result}")

# task 10
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
words_list = ["Hi","Hello","Good morning"]

def longest_word(words):
    longest = words
    for word in words_list[0:]:
        if len(word) > len(longest):
            longest = word 
    return longest

result = longest_word(words_list)
print(f"Longest word from list is: {result}")
