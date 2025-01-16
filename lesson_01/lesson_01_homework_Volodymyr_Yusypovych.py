# Домашня робота 1.1 ЮСИПОВИЧ ВОЛОДИМИР

# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
word_one = "Hello"
word_two = "world"
if True:
    print(f"{word_one} {word_two}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
apples_ammount = 2
banana_ammount = apples_ammount * 4
print ("Apples :", apples_ammount, "\n", "Banana :", banana_ammount)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("Perimeter of the figure from task 05 =",perimetery)

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
all_trees = apple_tree + pear_tree + plum_tree
print ("Total ammount of trees :", all_trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
noon_temperature = 5
after_noon_temperature = noon_temperature - 10
evening_temperature = after_noon_temperature + 4
print ("Evening temperature :", evening_temperature)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
present_boys = boys - 1
present_girls = girls - 2
present_childer = present_boys + present_girls
print ("Total ammont of children who is present in the theater group :", int(present_childer))

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book / 2)+(second_book / 2)
total_three_books = first_book + second_book + third_book
print ("Total ammount of books boughet in on example :", total_three_books)