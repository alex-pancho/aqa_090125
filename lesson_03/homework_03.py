alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?" \n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


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
black_sea_area = 436_402
azov_sea_area = 37_800
black_sea_and_azov_sea_area = black_sea_area + azov_sea_area
print( "The Black and Azov Seas together cover an area of: ", black_sea_and_azov_sea_area, " km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods_on_warehouses = 375_291
first_and_second_warehouses = 250_449
second_and_third_warehouses = 222_950

third_warehouse = total_goods_on_warehouses - first_and_second_warehouses
second_warehouse = second_and_third_warehouses - third_warehouse
first_warehouse = first_and_second_warehouses - second_warehouse 

output_task_05 = f"The first warehouse has {first_warehouse} products, the second has {second_warehouse} products," \
    f"and the third has {third_warehouse} products."
print (output_task_05)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
months = 18
total_price_of_computer = monthly_payment * months

print("The total price of the computer is: ", total_price_of_computer, " UAH")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

output_task_07 = f"a) 8019 : 8 = {8019 % 8}\n" \
    f"b) 9907 : 9 = {9907 % 9}\n" \
    f"c) 2789 : 5 = {2789 % 5}\n" \
    f"d) 7248 : 6 = {7248 % 6}\n" \
    f"e) 7128 : 5 = {7128 % 5}\n" \
    f"f) 19224 : 9 = {19224 % 9}\n"
print(output_task_07)

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

pizza_large = 274
pizza_medium = 218
juice = 35
cake = 350
water = 21
total_price = (pizza_large * 4) + (pizza_medium * 2) + (juice * 4) + cake + (water * 3)
print("The total price of the order is: ", total_price, " UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
photos_per_page = 8
pages = photos // photos_per_page
if photos % photos_per_page:
    pages += 1
print("Igor will need ", pages, " pages to paste all the photos")

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

distance = 1600
fuel_consumption = 9
tank_capacity = 48
fuel_needed = (distance / 100) * fuel_consumption
reffils = fuel_needed / tank_capacity
if fuel_needed % tank_capacity:
    reffils += 1
output_task_10 = f"The family needs {int(reffils)} full tanks, but the first refueling is done before the trip." \
     f" This means that {int(reffils) - 1} additional refueling stops will be required during the trip."
print(output_task_10)