# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("task 1")
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
        print(str(multiplier) + "x" + str(number) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
print("")
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
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(2, 3), end="\n \n")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("task 3")
def average_of_list(lst):
    return sum(lst) / len(lst)
print(average_of_list([1, 2, 3, 4, 5, 6]), end="\n \n")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("task 4")
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello, word!"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("task 5")
def longest_word(lst):
    return max(lst, key=len)
print(longest_word(["Hello", "word", "world", "Python", "programming"]), end="\n \n")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("task 6")
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2), end = "\n \n") # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

print("task 7")
def sum_of_nmbers():
    """Adds up all the natural numbers you enter until you enter 0 and returns the sum."""
    sum_ = 0
    while True:
        number = int(input("Enter a natural number: "))
        if number == 0:
            break
        sum_ += number
    return sum_ 

print(sum_of_nmbers(), end="\n \n")

print("task 8")
def sum_of_digits_of_number():
    """Calculates the sum of all digits of a natural number entered by the user."""
    number = input("Enter a natural number: ")
    sum_int = 0
    for digit in number:
        sum_int += int(digit)
    return sum_int 

print(sum_of_digits_of_number(), end="\n \n")

print("task 9")
def guess_the_number():
    """Implements the game “Guess the number” with 5 attempts to guess a random number from 1 to 20."""
    import random
    secret_number = random.randint(1, 20)
    guesses = 0
    max_guesses = 5
    print("Guess the number from 1 to 20 in 5 attempts!")

    for number in range(max_guesses):
        guess = int(input("Enter your guess: "))
        guesses += 1
        if guess < secret_number:
            print("Your guess is too small!")
        elif guess > secret_number:
            print("Your guess is too big!")
        elif guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {guesses} attempts!")
            break
    else:
        print("You didn't guess the number:(")
        print(f"The correct number was {secret_number}")

guess_the_number()
print("")

print("task 10")
def sum_of_even_numbers(numbers: list):
    """Calculates the sum of all EVEN numbers in the list."""
    sum_of_even = sum([num for num in numbers if num % 2 == 0])
    return sum_of_even 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers), end="\n \n")
