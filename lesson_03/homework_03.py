alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n"'
                       'Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
# messages_array = alice_in_wonderland.split('\n')
#
# # Це скоріш за все занадто, але мені було цікаво динамічно назначити змінні.
# for number, temp_message in enumerate(messages_array, 1):
#     locals()["_".join(['message', str(number)])] = temp_message
#
# # Зараз є декілька фізичних ліній (змінних) в локальній області.
# variables_list = [element for element in locals() if str(element).startswith('message_')]
#
# for variable in variables_list:
#     print(f"{variable}: {locals()[variable]}")

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
black_sea_size = 436402
azov_sea_size = 37800
summary_sea_size = black_sea_size + azov_sea_size
print(f"Сумарна площа Чорного і Азовського морів: {summary_sea_size} км2.")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
store_2 = (250449 + 222950) - 375291
store_1 = 250449 - store_2
store_3 = 222950 - store_2
print(f"Склад 1: {store_1},\nСклад 2: {store_2},\nСклад 3: {store_3}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
computer_total_cost = 1179 * 18
print(f"Повна вартість компьютера: {computer_total_cost} грн.")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(variable_a := 8019 % 8)
print(variable_b := 9907 % 9)
print(variable_c := 2789 % 5)
print(variable_d := 7248 % 6)
print(variable_e := 7128 % 5)
print(variable_f := 19224 % 9)


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
big_pizza_cost = 274 * 4
medium_pizza_cost = 218 * 2
juice_cost = 35 * 4
cake_cost = 350
bottled_water_cost = 21 * 3
total_amount = big_pizza_cost + medium_pizza_cost + juice_cost + cake_cost + bottled_water_cost
print(f"Всього знадобиться грошей: {total_amount} грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
fotos_quantity = 232
fotos_per_page = 8

if fotos_quantity % fotos_per_page == 0:
    pages_quantity = fotos_quantity // fotos_per_page
else:
    page_quantity = fotos_quantity // fotos_per_page + 1

# Строго кажучи, "page_quantity" в даному випадку може бути від 29 до 232 т.я. він може розміщувати по одній фото
# на сторінці.


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
gasoline_amount = 16 * 9
pit_stop_quantity = gasoline_amount // 48 - 1 if gasoline_amount % 48 == 0 else gasoline_amount // 48
print(f"Знадобиться {gasoline_amount} л пального.")
print(f"Під час поїздки треба буде заїхати на заправку {pit_stop_quantity} разів.")
