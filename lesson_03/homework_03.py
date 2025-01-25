# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# # task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# # task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# # task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = f'"Would you tell me, please, which way I ought to go from here?"'\
    f'"That depends a good deal on where you want to get to," said the Cat.'\
    f'"I don\'t much care where ——" said Alice.'\
    f'"Then it doesn\'t matter which way you go," said the Cat.'\
    f'"—— so long as I get somewhere," Alice added as an explanation.'\
    f'"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_see_area = 436_402
azov_see_area = 37_800

print(f'The Black Sea and Azov Sea together occupy an area of {black_see_area + azov_see_area} square kilometers.')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

warehouse_1 = 375_291 - 222_950
warehouse_3 = 375_291 - 250_449
warehouse_2 = 375_291 - warehouse_1 - warehouse_3

print (f'На першому складі розміщено {warehouse_1} товарів.'\
   f'На другому складі розміщено {warehouse_2} товарів.'\
   f'На третьому складі розміщено {warehouse_3} товарів.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
payment_time = 18

price = monthly_payment * payment_time
print (f'Computer price is {price}')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

numbers = [8019, 9907, 2789, 7248, 7128, 19224]
divisors = [8, 9, 5, 6, 5, 9]

for i in range(len(numbers)):
    print(numbers[i] % divisors[i], end=' ')
print()

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274
big_pizza_amount = 4
medium_pizza_price = 218
medium_pizza_amount = 2
juice_price = 35
juice_amount = 4
cake_price = 350
watter_price = 21
watter_amount = 3

total_price = big_pizza_price*big_pizza_amount + medium_pizza_price*medium_pizza_amount + juice_price*juice_amount + cake_price + watter_price*watter_amount

print (f'Tooal price is {total_price}')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

page_capacity = 8
photos_amount = 232

pages_required = photos_amount/page_capacity

print (f'Igor will need {pages_required:.0f} full pages.')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

treep_distance = 1600
fuel_consumption_per_100 = 9
tank_capacity = 48

fuel_per_treep = (treep_distance/100) * fuel_consumption_per_100
min_fuel_refill = fuel_per_treep/tank_capacity

print (f'The trip will require {fuel_per_treep} liters of fuel.'
    f'Minimum {min_fuel_refill} fuel refill per treep needed.')