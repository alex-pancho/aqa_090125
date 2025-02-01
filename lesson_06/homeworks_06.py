# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'green'
if alien_color == 'green':
    print('The alien has earned 5 points')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'red'
if alien_color == 'green':
    print('The alien has earned 5 points')
else:
    print('The alien has earned 10 points')

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print('The alien has earned 5 points')
elif 'red' in alien_colors:
    print('The alien has earned 15 points')
else:
    print('The alien has earned 10 points')

for i in alien_colors:
    if i == 'green':
        print('The alien has earned 5 points')
    elif i == 'red':
        print('The alien has earned 15 points')
    else:
        print('The alien has earned 10 points')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_toppings = input(f'Enter pizza toppings:').split(', ')
for pizza_topping in pizza_toppings:
    if pizza_topping == 'quit':
        break
    print(f"Add {pizza_topping=} to the pizza toppings")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
natural_number = input(f'Enter natural number:')
sum_numbers = 0
for number in natural_number:
    sum_numbers += int(number)
print(f"{sum_numbers=}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

# first variant
number = int(input(f'Enter number:'))
sum_numbers = number
while number != 0:
    number = int(input(f'Enter next number:'))
    sum_numbers += number
print(f'{sum_numbers=}')

# second variant
sum_numbers = 0
while True:
    number = int(input(f'Enter number:'))
    if number == 0:
        break
    sum_numbers += number
print(f'{sum_numbers=}')

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for i in range(max_guesses):
    guess = input("Enter a number: ")
    if int(guess) == secret_number:
        print("You are right!")
        break
    elif int(guess) > secret_number:
        print("Too high!")
    else:
        print("Too low!")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    print(f"{fruit=}")

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i ** 2 for i in numbers if i % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
