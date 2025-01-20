alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
    )
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

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
black_sea_square = 436402
azov_sea_square = 37800

total_sea_square = black_sea_square + azov_sea_square

print("Чорне та Азовське моря разом займають площу", total_sea_square, "км².")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
storage_1_and_2 = 250449
storage_2_and_3 = 222950

storage_1 = total_items - storage_2_and_3
storage_2 = storage_1_and_2 - storage_1
storage_3 = total_items - storage_1_and_2

print("На першому складі знаходиться", storage_1, "товарів.\n"
      "На другому складі знаходиться", storage_2, "товарів.\n"
      "На третьому складі знаходиться", storage_3, "товарів.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months_amount = 1.5 * 12
months_payment = 1179

computer_price = months_payment * months_amount

print("Вартість комп'ютера:", computer_price, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"Остача від ділення 8019 на 8: {a}, 9907 на 9: {b}, 2789 на 5: {c}, 7248 на 6: {d}, 7128 на 5: {e}, 19224 на 9: {f}")

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
big_pizza_total_price = 274 * 4
small_pizza_total_price = 218 * 2
juice_total_price = 35 * 4
cake_total_price = 350
water_total_price = 21 * 3

party_budget = big_pizza_total_price + small_pizza_total_price + juice_total_price + cake_total_price + water_total_price

print("Для святкування знадобиться", party_budget, "грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_amount = 232
photos_on_page = 8

pages_amount = photo_amount // photos_on_page

print("Ігорю знадобиться", pages_amount, "сторінок, щоб вклеїти всі фото")

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
petrol_per_100_km = 9
tank_capacity = 48

petrol_per_distance = 1600 * 9 / 100
petrol_filling_amount = petrol_per_distance / tank_capacity

print("Для поїздки знадобиться", petrol_per_distance, "літрів бензину")
print("Щонайменше необхідно заправитися", int(petrol_filling_amount), "рази")
