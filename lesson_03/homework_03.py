#Потенциально вижу 2 вариант, хочется уточнить, оба ли они правильные?
#Первый вариант.
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
#Второй вариант
alice_in_wonderland_01 ='''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough.
'''
print(alice_in_wonderland_01)
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
Black_sea = 436402
Azov_sea = 37000
Total_area = Black_sea + Azov_sea
print("Площа, яку займає Чорне та Азовське моря разом сягає", Total_area,"km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
#Объявляем переменные по нашим данным.
All_storage = 375291
Second_and_First_storage = 250449
Second_and_Third_storage = 222950
#Считаем переменные по нашим данным.
Second_storage = Second_and_First_storage + Second_and_Third_storage - All_storage
Third_storage = Second_and_Third_storage - Second_storage
First_storage = Second_and_First_storage - Second_storage
#Выводим переменные по нашим данным.  
print("Кількість товарів на першому складі -",First_storage,"од.")
print("Кількість товарів на другому складі -",Second_storage,"од.")
print("Кількість товарів на третьому складі -",Third_storage,"од.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Вводим переменную
Monthly_payment = 1179
Months = 12 * 1.5
Final_price_of_PC = Monthly_payment * Months
print("Кінцева вартість комп'ютера Михайла -",int(Final_price_of_PC),"грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
#Вычесляем каждый результат с помощью %
result_a = 8019 % 8
result_b = 9907 % 9
result_c = 2789 % 5
result_d = 7248 % 6
result_e = 7128 % 5
result_f = 19224 % 9
#Выводим конечный результат каждой переменной с новой строки.
print(f"a) {result_a}\nb) {result_b}\nc) {result_c}\nd) {result_d}\ne) {result_e}\nf) {result_f}")

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
#Объявляем переменные и вычисляем их значения.
Big_pizza = 274 * 4
Middle_pizza = 218 * 2
Juice = 35 * 4
Cake = 350
Water = 21 * 3
#Суммируем конечный результат каждой переменной и выводим результат.
print("Загальна сума за замовлення -", Big_pizza+Middle_pizza+Juice+Cake+Water)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
#Объявляем переменную
All_photos = 232
One_page = 8
Total_photos = All_photos / One_page
#Выводим конечный результат
print(int(Total_photos), "сторінок знадобиться Ігорю, щоб вклеїти всі фото")

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
#Объявляем перемененные
All_distance = 1600
Fuel_consuption = 100/9
Tank_volume = 48
#Выводим результаты, в зависимости от задания.
print(int(All_distance/Fuel_consuption),"літра знадобиться для всієї подорожі")
print(int(All_distance/(Tank_volume *Fuel_consuption))-1,"повних бака знадобиться для всієї подорожі, при умові, що виїхали в подорож з повним баком")


