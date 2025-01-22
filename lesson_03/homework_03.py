# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want'
    ' to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you '
    'go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do '
    'that," said the Cat, "if you only walk long enough."'
)
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

black_sea_area = 436402
azov_sea_area = 37800

total_seas_area = black_sea_area + azov_sea_area
print(f"{total_seas_area=} km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

sum_first_second_warehouse_products_count = 250449
sum_second_third_warehouse_products_count = 222950
sum_first_second_third_warehouse_products_count = 375291

third_warehouse_products_count = (
        sum_first_second_third_warehouse_products_count - sum_first_second_warehouse_products_count
)
second_warehouse_products_count = sum_second_third_warehouse_products_count - third_warehouse_products_count

first_warehouse_products_count = sum_first_second_warehouse_products_count - second_warehouse_products_count

print(f"Products in first warehouse are: {first_warehouse_products_count}")
print(f"Products in second warehouse are: {second_warehouse_products_count}")
print(f"Products in third warehouse are: {third_warehouse_products_count}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
computer_price_per_month = 1179
period = 12 * 1.5
total_compyter_price = computer_price_per_month * period
print(f"Total computer price is {total_compyter_price} UAH")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

# second variant
print(
    f"a) 8019 : 8 = {8019 % 8},\nb) 9907 : 9 = {9907 % 9},\nc) 2789 : 5 = {2789 % 5},\n"
    f"d) 7248 : 6 = {7248 % 6},\ne) 7128 : 5 = {7128 % 5},\nf) 19224 : 9 = {19224 % 9}",
)

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

big_pizza_count = 4
big_pizza_price = 274

middle_pizza_count = 2
middle_pizza_price = 218

juice_count = 4
juice_price = 35

cake_count = 1
cake_price = 350

water_count = 3
water_price = 21

total_products_price = (
        (big_pizza_count * big_pizza_price) + (middle_pizza_count * middle_pizza_price) + (juice_count * juice_price) +
        (cake_count * cake_price) + (water_count * water_price)
)
print(f"{total_products_price=} UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo_count = 232
max_photo_count_per_page = 8
page_count_with_photo = total_photo_count / max_photo_count_per_page
print(f"{page_count_with_photo=}")

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
gasoline_liters_per_100_km = 9
fuel_tank_capacity = 48

total_gasoline_liters_for_distance = gasoline_liters_per_100_km * (distance / 100)
stop_count = (total_gasoline_liters_for_distance / fuel_tank_capacity) - 1  # the gas tank will be full before leaving

print(f"{total_gasoline_liters_for_distance=}, \n{stop_count=}")
