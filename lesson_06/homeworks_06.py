# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'green'
if alien_color == 'green':
    print("5 points are achieved")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'yellow'
if alien_color == 'green':
    print("5 points are achieved")
else:
    print("10 points are achieved")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = {'green', 'yellow', 'red'}
current_alien_color = 0
for current_alien_color in alien_color:
    
    if current_alien_color == 'green':
        print("5 points are achieved")
    elif current_alien_color == 'red':
        print("15 points are achieved")
    else:
        print("10 points are achieved")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Pleas enter toppings for your pizza. \n To QUIT enter \'quit\'")
    
    if pizza_topping == 'quit':
        break
    print (f"Topping: {pizza_topping} will be added to your pizza")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
numbers_total = 0
entered_number = input("Pleas enter your number:")

for digits in entered_number:
    numbers_total += int(digits)
print (f"Sum of enterd digits: {entered_number}: {numbers_total}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
entered_number_total =0
while True:
    entered_number = input("Pleas enter any number exept \'0\'. \n  \'0\' will sumup all entered numbers")
    if entered_number == '0':
        break
    entered_number_total += int(entered_number)
print (f"Total of your's entered numbers is : {entered_number_total}")

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
for guesses in range(max_guesses):
    guess = int(input("Введіть своє припущення: "))
    
    if guess < secret_number:
        print("Припущення занадто мале")
    elif guess > secret_number:
        print("Припущення занадто велике")
    else:
        print(f"Вітаємо! Ви вгадали число.")
        break 

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
propper_fruits = 0
for propper_fruits in fruits:
    if propper_fruits == 'orange':
        continue
    print(propper_fruits)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [tup_number ** 2 for tup_number in numbers if tup_number % 2 == 0]
print("The list of squares of even numbers from the list will be:",result)  #  [4, 16, 36, 64, 100]
