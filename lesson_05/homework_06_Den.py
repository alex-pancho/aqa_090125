# # # task 1
# # """  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
# # Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
# # Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
# # Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
# # """
alien_color = 'green'
congratulations_massage = "Congratulations to you, defender of our planet and democracy in space."
insulting_massage = "You`ve shot a alien-scum!"
for_alien_massege = "You must be an alien yourself. Get a taste of lead democracy, scumbag!!!"
point_5_massage = "Get 5 points."
point_10_massage = "Get 10 points."
point_15_massage = "Get 15 points."
gap = "\n"
if alien_color == 'green':
    print(congratulations_massage, gap, insulting_massage, gap,point_5_massage, gap * 3)

# # task 2
# """  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
# Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
# Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
# Зробіть так, щоб виводилася умова else.
# """
alien_color = 'red'
if alien_color == 'green':
    print(congratulations_massage, gap, insulting_massage, gap,point_5_massage, gap *3)
else:
    print(congratulations_massage, gap, insulting_massage,gap, point_10_massage, gap *3)

# # task 3
# # task 4
# """  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
# змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
# Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
# Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
# Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
# + напишіть цикл for що перебере і обробить всі значення списку alien_color
# """
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print(congratulations_massage, gap, insulting_massage, gap,point_5_massage, gap * 3)
    elif color == 'red':
        print(congratulations_massage, gap,insulting_massage,gap, point_15_massage, gap * 3)
    elif color != 'green':
        print(congratulations_massage, gap, insulting_massage, gap, point_10_massage, gap * 3)
else:
    print(for_alien_massege, gap * 3)

# # task 5
# """  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
# для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
# надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
# """
pizza_toppings = []
while True:
    choice_of_topping = input("Введіть назву інгрідієнту, що бажаєте додати (або \'quit\' для завершеня замовлення) ")
    if choice_of_topping == "quit":
        break
    pizza_toppings.append(choice_of_topping)

print(f"Дякуємо за замовленя! До вашої піци буде додано: {' ,'.join(pizza_toppings)}. Приємного:))", gap * 3)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
user_data_number = input("Введіть натуральне, не дробове число, в десятичній системі, і ми підрахуєму суму його цифр: ")
list_of_numbers = list(user_data_number)
number_counter = 0
sum_of_numbers = 0
while number_counter < len(list_of_numbers):
    sum_of_numbers += int(list_of_numbers[number_counter])
    number_counter += 1
print(f"Сума цифр числа {user_data_number} становить: {sum_of_numbers}. Ну що, вгадали?", gap * 3)

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
list_of_calculated_numbers = []
sum_of_calculation = 0
while True:
    entered_number = input("Введіть ціле число, яке буде додано до підрахунку, або \"0\" для завершеня підрахунку і отриманя результату: ")
    entered_number = int(entered_number)
    if entered_number == 0:
        break
    list_of_calculated_numbers.append(entered_number)
for number in list_of_calculated_numbers:
    sum_of_calculation += number
print(f"Сума введених чисел {list_of_calculated_numbers} дорівнює: {sum_of_calculation}", gap)

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
for guesses in range(guesses, max_guesses):
    guesses += 1
    user_attempt = input(f"Поїхали, твоя {guesses} спроба: ")
    user_attempt = int(user_attempt)
    if user_attempt == secret_number:
        print(f"Оце так вдача! Ви вгадали з {guesses} спроби. Число було справді: {secret_number}")
    elif user_attempt < secret_number:
        guesses += 1
        print(f"От халепа! Але не засмучуйтесь, спробуйте ввести трохи більше число")
    elif user_attempt > secret_number:
        guesses +=1
        print(f"От халепа! Але не засмучуйтесь, спробуйте ввести трохи меньше число")
    else:
        print("System error: Sorry, something went wrong.")
print(gap * 3)

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit, gap * 3)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["Відповідь вставте сюди"]
print(result)  # [4, 16, 36, 64, 100]

result = [number ** 2 for number in numbers if number % 2 == 0]
print(result)
