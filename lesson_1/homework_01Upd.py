# task 01 == Виправте синтаксичні помилки > done
print("Hello world!")


# task 02 == Виправте синтаксичні помилки > done
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print > done
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була > upd
# завжди в чотири рази більша, ніж яблук
apples = 1
banana = apples * 4
print('Banana:', banana)

# task 05 == виправте назви змінних > done
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 > done
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print('Perimetery =', perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07 > done
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
garden = apple_tree + pear_tree + plum_tree
print('Garden tree:', garden)

# task 08 > done
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_morning = 5
temp_afternoon = temp_morning - 10
temp_evening = temp_afternoon + 4
print('Evening temperature:', temp_evening)

# task 09 > done
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
boys_today = boys - 1
girls_today = girls - 2
today_attendance = (boys_today + girls_today)
print("Today's attendance:", int(today_attendance))

# task 10 > done
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_price_1 = 8
book_price_2 = book_price_1 + 2
book_price_3 = (book_price_1 + book_price_2) / 2
print('Total book price:', book_price_1 + book_price_2 + book_price_3)