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
            print("The result is greater than 25")
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
print("_________________________________________________________________________")

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("task 2")
def add(a, b):
    return a + b
print("Сума чисел 3 та 5 дорівнює", add(3, 5))
print("_________________________________________________________________________")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("task 3")
def average(lst):
    if not lst:
        print("Список пустий")
        return 0
    return sum(lst) / len(lst)
print(average([1, 2, 3, 4, 5])) # повинно повернути 3.0
print("Середнє арифметичне чисел 1, 2, 3, 4, 5 дорівнює", average([1, 2, 3, 4, 5]))
print("_________________________________________________________________________")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("task 4")
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello, world!")) # поверне "!dlrow ,olleH"
print("_________________________________________________________________________")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("task 5")
def longest_word(words):
    return max(words, key=len)
print(longest_word(["apple", "banana", "cherry"])) # поверне "banana"
print("_________________________________________________________________________")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("task 6")

def find_substring(str1, str2):
    return str1.find(str2)  # Використовуємо вбудований метод find()

# Тестові випадки
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # Повинно повернути 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # Повинно повернути -1
print("_________________________________________________________________________")

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print("task 7, 8, 9, 10")
print("task 10.1")
def alien_points(alien_color: str):
    """
    Функція визначає кількість балів, яку заробив гравець в залежності від кольору прибульця.
    
    :param alien_color: Колір прибульця.
    :return: Кількість зароблених балів.
    """
    if alien_color == "green":
        return 5
    else:
        return 10
print(alien_points("green"))  # повинно повернути 5
print(alien_points("red"))  # повинно повернути 10
print("_________________________________________________________________________")

print("task 10.2")
def pizza_toppings():
    """
    Функція запитує користувача про начинки для піци та повертає список обраних начинок.
    
    :return: Список начинок для піци.
    """
    toppings = []
    while True:
        topping = input("Введіть начинку для піци (або 'quit' для виходу): ")
        if topping.lower() == 'quit':
            break
        toppings.append(topping)
    return toppings
print(pizza_toppings())
print("_________________________________________________________________________")

print("task 10.3")
def sum_digits_of_number(number):
    """
    Функція обчислює суму всіх цифр числа.
    
    :param number: Число, яке вводить користувач.
    :return: Сума цифр числа.
    """
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits
print(sum_digits_of_number(12345))  # повинно повернути 15
print("_________________________________________________________________________")

print("task 10.4")
def guess_number():
    """
    Функція реалізує гру "Вгадай число".
    Гравець має 5 спроб відгадати випадкове число від 1 до 20.
    
    :return: Результат гри.
    """
    import random
    secret_number = random.randint(1, 20)
    guesses = 0
    max_guesses = 5
    print("Вгадайте число від 1 до 20 за 5 спроб!")
    for i in range(max_guesses):
        guess = int(input("Введіть число: "))
        guesses += 1
        if guess < secret_number:
            print("Загадане число більше")
        elif guess > secret_number:
            print("Загадане число менше")
        else:
            return f"Ви вгадали число {secret_number} за {guesses} спроб"
    return f"Ви не вгадали. Загадане число було {secret_number}"
print(guess_number())
print("_________________________________________________________________________")


