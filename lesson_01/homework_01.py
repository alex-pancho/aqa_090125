# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
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
bananas = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(f"{perimetery=}")


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
apple_trees_count = 4
pear_trees_count = apple_trees_count + 5
plum_trees_count = apple_trees_count - 2
total_trees_count = apple_trees_count + pear_trees_count + plum_trees_count
print(f"{total_trees_count=}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
before_lunch_temperature = 5
after_lunch_temperature = before_lunch_temperature - 10
evening_temperature = after_lunch_temperature + 4
print(f"{evening_temperature=}")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
total_boys_count = 24
total_girls_count = total_boys_count//2

sick_boys_count = 1
absent_girls_count = 2

present_children_count = (total_boys_count + total_girls_count) - (sick_boys_count + absent_girls_count)
print(f"{present_children_count=}")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price)//2

all_books_price = first_book_price + second_book_price + third_book_price
print(f"{all_books_price=}")
