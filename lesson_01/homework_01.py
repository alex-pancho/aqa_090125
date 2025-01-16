# task 01 == Виправте синтаксичні помилки
print("task 01")
print("Hello", end = " ")
print("world!")
print("\n")

# task 02 == Виправте синтаксичні помилки
print("task 02")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
print("\n")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("task 03")
for letter in "Hello world!":
    print()
print("\n")

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("task 04")
apples = 2
banana = apples*4
print("\n")

# task 05 == виправте назви змінних
print("task 05")
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
print("storona_1 =", storona_1, "," "storona_2 =", storona_2, "," "storona_3 =", storona_3, "," "storona_4 =", storona_4)
print("\n")

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("task 06")
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("периметр фігури=",perimetery)
print("\n")

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("task 07")
apples = 4
pear = apples+5
plum = apples-2
allTree =  apples+pear+plum
print("apples =", apples, ",", "pear =", pear, ",", "plum =", plum)
print("всього посадили дерев ", allTree)
print("\n")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("task 08")
tempBeforeLunch = 5
tempAfterLunch = tempBeforeLunch-10
tempEvening = tempAfterLunch+4
print("температура надвечір ", tempEvening)
print("\n")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("task 09")
boys = 24
girls = int(24/2)
boysToday = boys-1
girlsToday = girls-2
allKidsToday = boysToday+girlsToday
print("у театральному гуртку сьогодні", allKidsToday, "дитини")
print("\n")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("task 10")
book1 = 8
book2 = book1+2
book3 = int((book1+book2)/2)
allBooks = book1+book2+book3
print("Перша книжка коштує ", book1, "грн.,", "друга книжка коштує ", book2, "грн.,", "третя книжка коштує ", book3,"грн.")
print("усі книги будуть коштувати ", allBooks, "грн.")
