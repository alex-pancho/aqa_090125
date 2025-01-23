
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
text_gap = "\n" * 3
print(alice_in_wonderland, text_gap)
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
area_units_of_measurement = " км2"
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
task_04_solution = f"Площа Чорного моря становить {black_sea_area}{area_units_of_measurement}.\n" \
    f"площа Азовського моря становить {azov_sea_area}{area_units_of_measurement}.\n" \
    f"Щоб обрахувати загальну площу морів їх потрібно просто додати - {black_sea_area} + {azov_sea_area} = {total_area}{area_units_of_measurement}"
print(task_04_solution, text_gap)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
product_units_of_measurement = " товара(ів)"
total_products = 375291
warehouse_1 = total_products - 222950
warehouse_3 = total_products - 250449
warehouse_2 = total_products - (warehouse_1 + warehouse_3)
task_05_solution = f"Є три склади мережі на яких містиця взагалом {total_products}{product_units_of_measurement}. \n" \
    f"Нам відомо, що на першому та другому складах перебуває 250 449 товарів. Тож можему обчислити товари третього складу. \n" \
    f"Для цього віднімемо від загальної кількості товарів товари, що знаходяться на другому та першому складі - {total_products} - 250449 = {warehouse_3}{product_units_of_measurement}. \n" \
    f"Також відомо, що yа другому та третьому складах – 222 950 товарів. Таким самим чином обчислюємо перший склад - {total_products} - 222950 = {warehouse_1}{product_units_of_measurement}. \n" \
    f"То ж, тепер можемо дізнатись скільки товарів на першому складі, віднявши від загальної кількості продуктів, продукти 2го + 3го складу: \n" \
    f"{total_products} - {warehouse_2} + {warehouse_3} = {warehouse_1} \n" \
    f"Одже відповідь: склад №1 - {warehouse_1}{product_units_of_measurement}, склад№2 - {warehouse_2}{product_units_of_measurement}, склад №3 - {warehouse_3}{product_units_of_measurement}"
print(task_05_solution, text_gap)
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
period_units_of_measurement = " місяць(ів)"
payment_units_of_measurement = " грн."
payment_period = 1.5 * 12
payment_amount = 1179
computer_price = payment_period * payment_amount
task_06_solution = f"Для початку пропоную порахувати скільки місяців треба сплачувати. Якщо в році 12 місяців то - 12 * 1.5 = {payment_period}{period_units_of_measurement} \n" \
    f"А тепер просто помножимо місяцний платіж на кількість місяців: {payment_period} * {payment_amount} = {computer_price}{payment_units_of_measurement} \n"
print(task_06_solution, text_gap)
# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
result_a = 8019 % 8
result_b = 9907 % 9
result_c = 2789 % 5
result_d = 7248 % 6
result_e = 7128 % 5
result_f = 19224 % 9
# Я плохо себе представляю реализацию этой задачи "как для школьника"\"как на бумажке в столбик". Будем считать "школьник" начал учить питон
task_07_solution = f"Остача від ділення чисел знаходиться за допомогою символа %. Це означає, що ми ділимо числа \n" \
    f"і дивимось, що залишиться після повного поділу.\n" \
    f"a) 8019 % 8 = {result_a}\n" \
    f"b) 9907 % 9 = {result_a}\n" \
    f"c) 2789 % 5 = {result_a}\n" \
    f"d) 7248 % 6 = {result_a}\n" \
    f"e) 7128 % 5 = {result_a}\n" \
    f"f) 19224 % 9 = {result_a}\n"
print(task_07_solution, text_gap)

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
cost_units_of_measurement = " грн."
quantity_units_of_measurement = " шт."
pizza_large_cost = 274
pizza_large_quantity = 4
pizza_medium_cost = 218
pizza_medium_quantity = 2
juice_cost = 35
juice_quantity = 4
cake_cost = 350
cake_quantity = 1
water_cost = 21
water_quantity = 3

# Обсчет стоимости каждого товара
pizza_large_total = pizza_large_cost * pizza_large_quantity
pizza_medium_total = pizza_medium_cost * pizza_medium_quantity
juice_total = juice_cost * juice_quantity
cake_total = cake_cost * cake_quantity
water_total = water_cost * water_quantity

total_birthday_price = (
    pizza_large_total +
    pizza_medium_total +
    juice_total +
    cake_total +
    water_total
)
task_08_solution = (
    f"Обрахуємо вартість кожного товару окремо:\n"
    f"- Велика піца: {pizza_large_quantity} * {pizza_large_cost} = {pizza_large_total}{cost_units_of_measurement}\n"
    f"- Середня піца: {pizza_medium_quantity} * {pizza_medium_cost} = {pizza_medium_total}{cost_units_of_measurement}\n"
    f"- Сік: {juice_quantity} * {juice_cost} = {juice_total}{cost_units_of_measurement}\n"
    f"- Торт: {cake_quantity} * {cake_cost} = {cake_total}{cost_units_of_measurement}\n"
    f"- Вода: {water_quantity} * {water_cost} = {water_total}{cost_units_of_measurement}\n"
    f"Загальна вартість замовлення: {total_birthday_price}{cost_units_of_measurement}\n"
)
print(task_08_solution, text_gap)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_units_of_measurement = " фото"
page_units_of_measurement = " сторінка(нок)"
photo_total_quantity = 232
page_capacity = 8
required_pages_quantity = photo_total_quantity + page_capacity / page_capacity
task_09_solution = (
    f"Щоб дізнатись кількість сторінок, потрібно загальну кількість фото {photo_total_quantity} "
    f"поділити на кількість фото на одній сторінці {page_capacity}. "
    f"Не забуваємо про округлення в більшу сторону, адже сторінка не може бути неповною.\n"
    f"Розрахунок: ({photo_total_quantity} / {page_capacity} = {required_pages_quantity}.\n"
    f"Отже, Ігорю потрібно {required_pages_quantity}{page_units_of_measurement}."
)
print(task_09_solution, text_gap)

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
track_units_of_measurement = " км."
fuel_units_of_measurement = " літра(ів)"
track = 1600
track_segment = 100
fuel_consumption = 9
tank_capacity = 48
total_liters_fuel = track / track_segment * fuel_consumption
total_refueling = track / (tank_capacity / fuel_consumption * track_segment)
task_10_solution = (
    f"1) Для розрахунку загальної кількості палива спочатку обрахуємо, скільки разів пройдемо "
    f"{track_segment} км відстані, помножимо на витрати палива на кожні 100 км:\n"
    f"{track} / {track_segment} * {fuel_consumption} = {total_liters_fuel}{fuel_units_of_measurement}.\n"
    f"\n2) Для кількості заправок потрібно поділити загальну кількість палива "
    f"на обсяг баку:\n"
    f"({total_liters_fuel} / {tank_capacity} = {total_refueling} раз(ів).\n"
    f"Отже, для подорожі родині знадобиться {total_liters_fuel}{fuel_units_of_measurement} бензину "
    f"та {total_refueling} заправок."
)
print(task_10_solution, text_gap)
