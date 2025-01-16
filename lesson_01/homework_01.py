# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"{apples} apples and {banana} bananas")

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4
perimetery = side_1 + side_2 + side_3 + side_4
print("P={}".format(perimetery))


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
apples=4
pears=apples+5
plums=apples-2
summ=apples+pears+plums
print ("Всього посадили %s дерев" %summ)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_morning=12
temperature_day=temperature_morning-10
temperature_evening=temperature_day+4
print ("Надвечір температура була %s°" %temperature_evening)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boy_all=24
girl_all=boy_all//2
absent=1+2
print ("Сьогодні " + str(girl_all+boy_all-absent) + " дитини у театральному гуртку")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1=8
book_2=book_1+2
book_3=(book_1+book_2)/2
three_books=book_1+book_2+book_3
hryvnias = int(three_books)  
kopecks = round((three_books - hryvnias)*100)
print(f"До оплати {hryvnias} гривень {kopecks:02d} копійок")