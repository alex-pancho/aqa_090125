
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)


single_quotes = [char for char in alice_in_wonderland if char == "'"]
print(f"Знайдено {len(single_quotes)} одинарних лапок: {single_quotes}")


print(alice_in_wonderland)


# task 04

black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print("Загальна площа Чорного та Азовського морів:", total_area, "км²")


# task 05
total_items = 375291
first_and_second = 250449
second_and_third = 222950
C = total_items - first_and_second  # З третього складу
A = total_items - second_and_third  # З першого складу
B = total_items - (A + C)            # З другого складу
print("Кількість товарів на першому складі:", A)
print("Кількість товарів на другому складі:", B)
print("Кількість товарів на третьому складі:", C)


# task 06


months = 1.5 * 12  # Півтора року = 18 місяців
monthly_payment = 1179  # Оплата за місяць у грн
total_cost = months * monthly_payment
print("Вартість комп'ютера:", total_cost, "грн")



# task 07
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("a) 8019 % 8 =", a)
print("b) 9907 % 9 =", b)
print("c) 2789 % 5 =", c)
print("d) 7248 % 6 =", d)
print("e) 7128 % 5 =", e)
print("f) 19224 % 9 =", f)




# task 08

items = {
    "Піца велика": (4, 274),  # (Кількість, Ціна за одиницю)
    "Піца середня": (2, 218),
    "Сік": (4, 35),
    "Торт": (1, 350),
    "Вода": (3, 21),
}
total_cost = sum(quantity * price for quantity, price in items.values())
print("Загальна вартість замовлення:", total_cost, "грн")


# task 09

photo = 232  
on_page = 8
pages = (photo + on_page - 1) // on_page
print(pages)



# task 10
distance = 1600  # Відстань між Харковом і Будапештом (км)
fuel_per_100km = 9  # Літрів бензину на 100 км
tank_capacity = 48  # Місткість баку (літри)

# 1) Обчислення кількості літрів бензину, що знадобляться для подорожі
total_fuel_needed = (distance / 100) * fuel_per_100km

# 2) Обчислення мінімальної кількості зупинок на заправку
stops_needed = total_fuel_needed / tank_capacity
stops_needed = int(stops_needed) if stops_needed.is_integer() else int(stops_needed) + 1

# Виведення результатів
print("1) Для подорожі знадобиться", total_fuel_needed, "літрів бензину.")
print("2) Родині потрібно заїхати на заправку мінімум", stops_needed, "рази.")

