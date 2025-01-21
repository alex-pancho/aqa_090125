# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland_01 = (""""Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don\'t much care where ——", said Alice.\n
"Then it doesn\'t matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough".\n""")

alice_in_wonderland_02 = f"—— Would you tell me, please, which way I ought to go from here?\n" \
    f"—— That depends a good deal on where you want to get to, said the Cat.\n" \
    f"—— I don\'t much care where.. , said Alice.\n" \
    f"—— Then it doesn\'t matter which way you go, said the Cat.\n" \
    f"—— .. so long as I get somewhere, Alice added as an explanation.\n" \
    f"—— Oh, you\'re sure to do that, said the Cat, if you only walk long enough.\n" \

alice_in_wonderland_03 = ("—— Would you tell me, please, which way I ought to go from here?\n"
                          "—— That depends a good deal on where you want to get to, said the Cat.\n"
                          "—— I don\'t much care where.. , said Alice.\n"
                          "—— Then it doesn\'t matter which way you go, said the Cat.\n"
                          "—— .. so long as I get somewhere, Alice added as an explanation.\n"
                          "—— Oh, you\'re sure to do that, said the Cat, if you only walk long enough.\n")
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(f"""Task 01 version 1
{alice_in_wonderland_01}""")

print(f"""Task 01 version 2
{alice_in_wonderland_02}""")

print(f"""Task 01 version 3)
{alice_in_wonderland_03}""")

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
print("task 04")
blackSeaArea = 436402
azovSeaArea = 37800
sumArea = blackSeaArea + azovSeaArea
uotputTask4 = f"Площа Чорного моря = {blackSeaArea} км2. "\
    f"Площа Азовського моря = {azovSeaArea} км2. " \
    f"Чорне та Азовське моря разом займають площу {sumArea} км2."
print(uotputTask4)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\n""task 05")
allItems = 375291
firstAndSecondStocks = 250449
secondAndThirdStocks = 222950
firstStock = allItems - secondAndThirdStocks
thirdStock = allItems - firstAndSecondStocks
secondStock = allItems - firstStock - thirdStock
outputTask5 = f"""Мережа супермаркетів має 3 склади, де всього розміщено {allItems} товар. 
На першому складі розміщено {firstStock} товар.
На другому складі розміщено {secondStock} товарів.
На третьому складі розміщено {thirdStock} товари."""
print(outputTask5)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("\n""task 06")
cost1Month = 1179
costAllMonth = cost1Month * 18
computerCost = f"""Михайло купує комп’ютер, скориставшись послугою «Оплата частинами».
Якщо сплачувати необхідно буде півтора року по 1179 грн/місяць,
то вартість комп’ютера складе {costAllMonth} грн"""
print(computerCost)


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("\n""task 07")
variableA = 8019 % 8
variableB = 9907 % 9
variableC = 2789 % 5
variableD = 7248 % 6
variableE = 7128 % 5
variableF = 19224 % 9
variableAA = 8019 / 8
variableBB = 9907 / 9
variableCC = 2789 / 5
variableDD = 7248 / 6
variableEE = 7128 / 5
variableFF = 19224 / 9

print(f"""a) 8019 : 8 = {variableAA}, на ціло на 8 ділиться число 8016, тому остачa від діленя є {variableA}
b) 9907 : 9 = {variableBB}, на ціло на 9 ділиться число 9900, тому остачa від діленя є {variableB}
c) 2789 : 5 = {variableCC}, на ціло на 5 ділиться число 2785, тому остачa від діленя є {variableC}
d) 7248 : 6 = {variableDD}, число ділиться на ціло, остачa від діленя є {variableD}
e) 7128 : 5 = {variableEE}, на ціло на 5 ділиться число 7125, тому остачa від діленя є {variableE}
f) 19224 : 9 = {variableFF}, число ділиться на ціло, тому остачa від діленя є {variableF}""")

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
print("\n""task 08")
pizzaBigCost = 274
pizzaMediumCost = 218
juiceCost = 35
cakeCost = 350
waterCost = 21
allCost = (pizzaBigCost * 4) + (pizzaMediumCost * 2) + (juiceCost * 4) + (waterCost * 3) + cakeCost
print(f"""Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити. 
Всього Ірині знадобиться {allCost} грн""")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("\n""task 09")
allPhoto = 232
photoMaxOnOnePage = 8
pagesMin = int(allPhoto/photoMaxOnOnePage)
print(f"У Ігора всього є {allPhoto} фотографій. "
      f"Якщо розмістити на одній сторінці {photoMaxOnOnePage} фото, то всьо Ігореві знадобиться {pagesMin} сторінок")

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
print("\n""task 10")
distance = 1600
capacity = 48
gasForAllDistance = int(distance/100)*9
gasStationVisit = int(gasForAllDistance/capacity)
print(f"""Родина зібралася в автомобільну подорож із Харкова в Будапешт. 
Відстань між цими містами становить 1600 км.
Якщо на кожні 100 км необхідно 9 літрів бензину, то всього для такої подорожі знадобиться {gasForAllDistance} літрів.
Якщо місткість баку становить 48 літрів, то щонайменше доведеться заїхати на заправку {gasStationVisit} рази.""")
