alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)

black_sea_area = 436402  # км²
azov_sea_area = 37800    # км²

total_area = black_sea_area + azov_sea_area
print(f"Чорне та Азовське моря разом займають {total_area} км².")

total_items = 375291
items_first_and_second = 250449
items_second_and_third = 222950


first_inventory = total_items - items_second_and_third
third_inventory = total_items - items_first_and_second
second_inventory = total_items - (first_inventory  + third_inventory)


print(f"На першому складі {first_inventory} товарів, на другому складі {third_inventory} товарів, на третьому складі {second_inventory} товарів.")

monthly_payment = 1179  # грн
months = 18             # півтора року = 18 місяців

total_cost = monthly_payment * months
print(f"Вартість комп'ютера становить {total_cost} грн.")

Ostacha_a = 8019 % 8
Ostacha_b = 9907 % 9
Ostacha_c = 2789 % 5
Ostacha_d = 7248 % 6
Ostacha_e = 7128 % 5
Ostacha_f = 19224 % 9

print(f"Остача від ділення 8019 : 8 буде {Ostacha_a}")
print(f"Остача від ділення 9907 : 9 буде {Ostacha_b}")
print(f"Остача від ділення 2789 : 5 буде {Ostacha_c}")
print(f"Остача від ділення 7248 : 6 буде {Ostacha_d}")
print(f"Остача від ділення 7128 : 5 буде {Ostacha_e}")
print(f"Остача від ділення 19224 : 9 буде {Ostacha_f}")


price_pizza_big = 274
qty_pizza_big = 4
price_pizza_middle = 218
qty_pizza_middle = 2
price_juice = 35
qty_juice = 4
price_cake = 350
qty_cake  = 1
price_water = 21
qty_water = 3

print(f"Витрати на велику піцу складуть {price_pizza_big} помножене на {qty_pizza_big}, що складає {price_pizza_big * qty_pizza_big} \n'"
      f"Витрати на середню піцу складуть {price_pizza_middle} помножене на {qty_pizza_middle}, що складає {price_pizza_middle * qty_pizza_middle} \n'"
      f"Витрати на сік складуть {price_juice} помножене на {qty_juice}, що складає {price_juice * qty_juice} \n'"
      f"Витрати на торт складуть {price_cake} помножене на {qty_cake}, що складає {price_cake * qty_cake} \n'"
      f"Витрати на воду складуть {price_water} помножене на {qty_water}, що складає {price_water * qty_water} \n'"
      f"Сумарні витрати складуть {(price_pizza_big * qty_pizza_big) + (price_pizza_middle * qty_pizza_middle) + (price_juice * qty_juice) + (price_cake * qty_cake) +(price_water * qty_water)}"
      )

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
photos_per_page = 8

pages_needed = total_photos // photos_per_page
print(f"Ігорю знадобиться {pages_needed} сторінок, щоб вклеїти всі фото.")

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
distance = 1600  # км
fuel_per_100_km = 9  # літри
tank_capacity = 48   # літри

# 1) Скільки літрів бензину потрібно
total_fuel_needed = (distance / 100) * fuel_per_100_km
print(f"Для подорожі потрібно {int(total_fuel_needed)} літрів бензину.")

# 2) Кількість заправок
refuels_needed = total_fuel_needed / tank_capacity
print(f"Якщо перед пригодою бак був пустий, родині потрібно буде заїхати на заправку  {int(refuels_needed)} рази.")

