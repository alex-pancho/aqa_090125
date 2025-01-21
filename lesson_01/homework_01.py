# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")
#але я би виконав простіше, використовуючи один з двох варіантів(в ідеалі 1й):
print("Hello world!")
print("Hello", "world!")


# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
#умова не доречна і завжди виконується, тож більш простий варіант:
hello = "Hello"
world = "world"
print(f"{hello} {world}!")


# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4 * apples


# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4


# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


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
apple = 4
pear = 5 * apple
plum = apple - 2
garden_amount = apple + pear + plum
print("garden amount = ", garden_amount)
# or
print("garden_amount = ", apple + pear + plum)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
t_before_lunch = 5
t_after_lunch = t_before_lunch - 10
t_evening = t_after_lunch + 4
print("evening temperature = ", t_evening)
# or
t_start = 5
t_second_measurement =  - 10
t_third_measurement = 4
t_evening = t_start + t_second_measurement + t_third_measurement
print("evening temperature = ", t_evening)


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
overall_guys = 24
overall_girls = overall_guys / 2
todays_guys = overall_guys - 1
todays_girls = overall_girls - 2
todays_quantity = todays_girls + todays_guys
print("todays presence - ", todays_quantity)
# or
overall_guys = 24
overall_group = overall_guys + overall_guys / 2
guys_absent = 1
girls_absent = 2
todays_quantity = overall_group - guys_absent - girls_absent
print("todays presence - ", todays_quantity)


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 - 2
book_3 = (book_1 + book_2) / 2
print(sum([book_1, book_2, book_3]))
# or
books_count = 4
if books_count < 1:
    total = None
    print("please choose your count")
elif books_count == 1:
    total = 8
elif books_count == 2:
    book_1 = 8
    book_2 = book_1 - 2
    total = book_1 + book_2
elif books_count == 3:
    book_1 = 8
    book_2 = book_1 - 2
    book_3 = (book_1 + book_2) / 2
    total = book_1 + book_2 + book_3
else:
    total = None
    print("You can not buy more then 3 books")
if total is not None:
    print("total amount =", total)
