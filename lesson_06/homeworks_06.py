alien_color = 'green'

if alien_color == 'green':
    print("Гравець щойно заробив 5 балів.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Гравець щойно заробив 5 балів.")
else:
    print("Гравець щойно заробив 10 балів.")

alien_colors = ['green', 'yellow', 'red']

for alien_color in alien_colors:
    if alien_color == 'green':
        print("Гравець щойно заробив 5 балів.")
    elif alien_color == 'red':
        print("Гравець заробив 15 очок.")
    else:
        print("Гравець щойно заробив 10 балів.")

while True:
    topping = input("Введіть начинку для піци (або 'quit' для завершення): ")
    if topping == 'quit':
        break
    print(f"Додаємо {topping} до вашої піци.")

# task 6
number = input("Введіть натуральне число: ")
sum_of_digits = 0
for digit in number:
     sum_of_digits += int(digit)
     rint(f"Сума цифр числа {12345}: {15}")




# task 7
total_sum = 0
while True:
     number = input("Введіть число (або 0 для завершення): ")
     if number == "0":
           total_sum += int(number)
           print(f"Сума всіх введених чисел: {total_sum}")
         
"""

# task 8
""" import random
secret_number = random.randint(1, 20)
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for attempt in range(1, max_guesses + 1):
     guess = int(input(f"Спроба {attempt}. Введіть ваше припущення: "))
    if guess < secret_number:
        print("Занадто мале число!")
    elif guess > secret_number:
        print("Занадто велике число!")
    else:
      print(f"Вітаємо! Ви вгадали число {secret_number} за {attempt} спроб!")

# task 9
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
      if fruit == "orange":
             continue  
       print(fruit)

# task 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]