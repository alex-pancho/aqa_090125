alice_in_wonderland = '"Would you tell me, please, which way I ought to go \
from here?"\n"That depends a good deal on where you want to get to," said the \
Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way \
you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh,\
you\'re sure to do that," said the Cat, "if you only walk long enough."'
print (alice_in_wonderland)
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
black_sea_area = [436_402, "km2"]
azov_sea_area = [37_800, "km2"]
sea_area_sum = black_sea_area[0] + azov_sea_area [0]
print (f"Area of ​​the Black and Azov sea combined equal {sea_area_sum} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.

"""
total_storages_count = 3
total_goods_count = 375_291
storage_one_plus_storage_two_goods = 250_449
storage_two_plus_storage_three_goods = 222_950
storage_one = total_goods_count - storage_two_plus_storage_three_goods
storage_two = storage_one_plus_storage_two_goods - storage_one
storage_three = storage_two_plus_storage_three_goods - storage_two
print ("Number of goods placed in the First storage is :", storage_one, "Number \
of goods placed in the Second storage is :", storage_two, "Number of goods placed \
in the Third storage is :", storage_three, sep= '\n') 

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
purches = 'Computer'
payment_duration = [18, "monthes"] # question regarding first payment
amount_per_month = [1_179, "UAH"]
purches_total_amount = payment_duration[0] * amount_per_month[0]
print (f"{purches} total amount will be {purches_total_amount} {amount_per_month[1]}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
task_a = 8019 % 8 
task_b = 9907 % 9
task_c = 2789 % 5
task_d = 7248 % 6
task_e = 7128 % 5
task_f = 19224 % 9
print(f"Remainder from dividing numbers for task a) {task_a}", f"Remainder from dividing \
numbers for task b) {task_b}",f"Remainder from dividing numbers for task c) {task_c}", 
f"Remainder from dividing numbers for task d) {task_d}",f"Remainder from dividing numbers \
for task e) {task_e}", f"Remainder from dividing numbers for task f) {task_f}",sep='\n')

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
big_pizza = [4 , 274, "UAH"]
medium_pizza = [2, 218, "UAH"]
juice = [4, 35, "UAH"]
cake = [1, 350, "UAH"]
water = [3, 21, "UAH"]
print('The total amount of money for the purchase due birthday will be {0:0d}'.format((big_pizza[0]
*big_pizza[1])+(medium_pizza[0]*medium_pizza[1])+(juice[0]*juice[1])+cake[1]+(water[0]*water[1])),'UAH')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_total_amount = 232
min_amount_photo_per_page = min (1,2,3,4,5,6,7,8)
max_amount_photo_per_page = max (1,2,3,4,5,6,7,8)
min_amount_of_pages = photo_total_amount / max_amount_photo_per_page
max_amount_of_pages = photo_total_amount / min_amount_photo_per_page
print("Ihor will need a minimum", int(min_amount_of_pages), "pages to a maximum",
int(max_amount_of_pages), "pages to place all his photos in the album.")

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
distance = 1600
gas_for_100_km = 9
gas_tank = 48
total_amount_of_gas = (distance//100) * gas_for_100_km
stops_per_trip = total_amount_of_gas / gas_tank 
stops_per_trip -= 1 #Let's assume that the car has a full tank of gas before the start
print(f"1) For all trip family will need {total_amount_of_gas} liters of the gas.", '\n'
"2) Count of stops that family will atlist need to do is", int(stops_per_trip), end='.')