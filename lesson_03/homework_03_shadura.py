
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
print(f"\n")

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
area_azov_sea = 436402
area_black_sea = 37800
area_azov_black = area_azov_sea + area_black_sea

print(f"Чорне море займає {area_black_sea} км2, Азовське море — {area_azov_sea} км2.")
print(f"Разом вони займають {area_azov_black} км2.")
print(f"\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# sklad_1 + sklad_2 = 250449
# sklad_2 + sklad_3 = 222950
# sklad_1 + sklad_2 + sklad_3 = 375291

sklad_3 = 375291 - 250449 
sklad_2 = 222950 - sklad_3
sklad_1 = 250449 - sklad_2

print(f"Kількість товарів, що розміщені на кожному складі:\n"
      f"Склад № 1: {sklad_1}\n"
      f"Склад № 2: {sklad_2}\n"
      f"Склад № 3: {sklad_3}\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
#18 months * 1179
total_price = 1179 * 18
print(f"Загальна вартість комп’ютера: {total_price} гривень\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
result_a = 8019 % 8
result_b = 9907 % 9
result_c = 2789 % 5
result_d = 7248 % 6
result_e = 7128 % 5
result_f = 19224 % 9

print("Остача від ділення:")
print("a) 8019 : 8 =", result_a)
print("b) 9907 : 9 =", result_b)
print("c) 2789 : 5 =", result_c)
print("d) 7248 : 6 =", result_d)
print("e) 7128 : 5 =", result_e)
print("f) 19224 : 9 =", result_f)
print ("\n ")

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
pizza_big_count = 4
pizza_big_price = 274

pizza_medium_count = 2
pizza_medium_price = 218

juice_count = 4
juice_price = 35

cake_count = 1
cake_price = 350

water_count = 3
water_price = 21


total_pizza_big = pizza_big_count * pizza_big_price
total_pizza_medium = pizza_medium_count * pizza_medium_price
total_juice = juice_count * juice_price
total_cake = cake_count * cake_price
total_water = water_count * water_price

total_cost = (total_pizza_big + total_pizza_medium + total_juice + total_cake + total_water)

print("Загальна сума замовлення:", total_cost, "грн")
print ("\n ")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
pages = total_photos // photos_per_page
if total_photos % photos_per_page != 0:
    pages += 1
print("Ігорю знадобиться", pages, "сторінок \n")



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
distance = 1600         # расстояние в км
fuel_per_100 = 9        # расход бензина: 9 литров на 100 км
tank_capacity = 48      # вместимость бака в литрах

# сколько литров бензина потребуется для всей поездки
total_fuel = (distance / 100) * fuel_per_100
# Для 1600 км: (1600 / 100) * 9 = 16 * 9 = 144 литров

additional_fuel = total_fuel - tank_capacity

stops = int(additional_fuel // tank_capacity)
if additional_fuel % tank_capacity != 0:
        stops += 1

print("Для подорожі потрібно:", total_fuel, "л.")
print("щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі:", stops)