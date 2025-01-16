# THIS IS UPDATED FILE
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
banana = apples*4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("task 05. Perimeter = ", perimetery , "\n")


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
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
all_trees = apple_trees + plum_trees + pear_trees
print("task 07. Відповідь: всього в саду посадили ", all_trees , " дерев\n")


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temp = 0 + 5
day_temp = morning_temp - 10
evening_temp = day_temp + 4
print("task 08. Відповідь: Температура ввечорі ", evening_temp , " градус\n")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
total_boys = 24
total_girls = total_boys // 2 # Цілочисельний поділ щоб виводити результат без дробової частини
total_children = total_boys + total_girls
today_girls = total_girls - 2 
today_boys = total_boys - 1
today_children_version_1 = total_children - 1 - 2 #Більш простий варіант
today_children_version_2 = today_boys + today_girls # Цей варінт більш корисний для подальшого використання

print("task 09. Відповідь: Сьогодні у гуртку ", today_children_version_1 , " дитини \n") 
print("task 09. Відповідь: Сьогодні у гуртку ", today_children_version_2 , " дитини \n") 

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
#Version 1
price_book_1 = 8
price_book_2 = price_book_1 + 2
price_book_3 = (price_book_1 + price_book_2) / 2 
total_book_price_v1 = price_book_1 + price_book_2 +price_book_3

print(f"task 10. Version1. Відповідь: усі книги, якщо купити по одному примірнику, будуть коштувати  {total_book_price_v1:.2f} гривень \n") #Форматування результату, 2 знаки після коми

#Version 2: враховує кількість книг
num_book_1 = 1
num_book_2 = 1
num_book_3 = 1
total_book_price_v2 = num_book_1 * price_book_1 + num_book_2 * price_book_2 + num_book_3 * price_book_3
print(f"task 10. Version2. Відповідь: усі книги разом будуть коштувати  {total_book_price_v2:.2f} гривень \n") 