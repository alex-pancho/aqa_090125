# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
print("\n", "task 1")

alien_color = "yellow"
if alien_color == "green":
    print("Ви виграли 5 балів")


# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
print("\n", "task 2")

if alien_color == "green":
    print("Ви виграли 5 балів")
else: print("Ви виграли 10 балів")


# task 3
print("\n", "task 3")

if alien_color == "green":
    print("Ви виграли 5 балів")
elif alien_color == "red":
    print("Ви виграли 15 балів")
else: print("Ви виграли 10 балів")


# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
print("\n", "task 4")

alien_color = ["yellow", "red", "green"]
for i in alien_color:
    if i == "green":
        print(f"Alien is {i}. Ви виграли 5 балів")
    elif i == "red":
        print(f"Alien is {i}. Ви виграли 15 балів")
    elif i == "yellow":
        print(f"Alien is {i}. Ви виграли 15 балів")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
print("\n", "task 5")

pizza_topping = input("Введіть назви начинoк для піци, введіть слово quit, коли всі бажані начинки будуть введені: ")
list_pizza_topping = []
while pizza_topping != "quit":
    list_pizza_topping.append(pizza_topping)
    print(f"начинка {pizza_topping} додана до замовлення")
    pizza_topping = input("Введіть назву начинки для піци: ")
else: print(f"Начинки {list_pizza_topping} будуть додані до вашої піци")


# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
print("\n", "task 6")

number = input("Введіть натуральне число: ")
counter = []

for i in number:
    counter.append(i)
    
sumCount = sum([int (i) for i in counter])
print(f"Сума цифр числа {number}: {sumCount}")


# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
print("\n", "task 7")

number = input("Введіть числа, введіть '0', коли всі бажані числа будуть введені: ")
numbers_list = []

while number != '0' :
    numbers_list.append(number)
    number = input("Введіть наступне число: ")
    if number == '0':
        break
        
sumCount = sum([int (i) for i in numbers_list])
print(f"Сума всіх введених чисел = {sumCount}")


# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
print("\n", "task 8")

import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
your_number = input("Введіть число: ")
your_number_int = int(your_number)
your_try = 1
while your_try < 5:
    if your_number_int < secret_number:
        print("Спробуй більше число")
        your_number = input("Введіть число: ")
        your_number_int = int(your_number)

    elif your_number_int > secret_number:
        print("Спробуй менше число")
        your_number = input("Введіть число: ")
        your_number_int = int(your_number)

    elif your_number_int == secret_number:
        print("Ти вгадав число!")
        break
    your_try += 1
else: print("Ти використав усі 5 спроб.")


# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
print("\n", "task 9")

fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in fruits:
    if i == "orange":
        continue
    print(i)


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
print("\n", "task 10")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i ** 2 for i in numbers if i % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]

# task 6.1
#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
print("\n", "task 6.1")

line = input("Введіть рядок символів: ")
set_line = set(line)
if len(set_line) > 10:
    print("True")
else:
    print("False")

#task 6.4
#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
print("\n", "task 6.4")

list_all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list = []
for i in list_all_numbers:
    if i % 2 == 0:
        sum_list.append(i)

result= sum(sum_list)
print(result)

#task 6.2
#Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
print("\n", "task 6.2")

word = input("Введіть слово, в якому є літера 'h' або 'H': ")
count_h = tuple(word).count("h")
count_H = tuple(word).count("H")
while count_h == 0 and count_H == 0:
    print("Слово не містить літеру 'h' або 'H', спробуйте ще раз")
    word = input("Введіть слово, в якому є літера 'h' або 'H': ")
    count_h = tuple(word).count("h")
    count_H = tuple(word).count("H")
else:
    print("Слово містить літеру 'h'")


