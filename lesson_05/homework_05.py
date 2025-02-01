small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("\n task 1")
unique_elements_in_small_list = set(small_list)
print(f'Всі унікальні елементи зі списку small_list: {unique_elements_in_small_list}')

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("\n task 2")
average_of_elements_in_small_list = sum(small_list) / len(small_list)
print(f'Середнє арифметичне всіх елементів списку small_list: {average_of_elements_in_small_list}')

# task 3. Перевірте, чи є в списку big_list дублікати
print("\n task 3")
if len(big_list) == len(set(big_list)): # перетворити список у сет та порівняти фактичну довжину списку і довжину отриманого сету
    print("У списку big_list немає дублікатів")
else:
    print("У списку big_list є дублікати")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("\n task 4")
max_key = max(add_dict)
print(f'Ключ із максимальним значенням у словнику add_dict: {max_key}')

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("\n task 5")
swap_dict_base_dict = {}
    # використаємо цикл for щоб повторити кожну пару ключа та значення 
    # за допомогою методу .items(),
    # який поверне пару кортежу ключа та значення.
for key, value in base_dict.items():
    swap_dict_base_dict[value] = key # створимо змінну, де ключ і значення будуть змінені місцями
print(swap_dict_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("\n task 6")
sum_dict = {}
for key in base_dict.keys(): # Перевірка на основі ключів зі словника base_dict
    if key in add_dict:  # Перевірити, чи ключ з base_dict є у словнику add_dict
        sum_dict = str(base_dict[key]) + str(add_dict[key]) # об'єднати значення ключів в одну строку
        print(sum_dict)

# task 7.
print("\n task 7")
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_of_symbols = set(line)
print(f'Множина всіх символів у рядку:\n{set_of_symbols}')

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("\n task 8")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
symmetric_differense_set = set_1 ^ set_2
print(f'Сума елементів двох множин = {sum(symmetric_differense_set)}')

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("\n task 9")
list_1 = {3, 5, 7, 9, 11, 12}
list_2 = {2, 3, 5, 8, 9, 12}
set_of_unique_elements = set(list_1).symmetric_difference(set((list_2)))
print(f'Оновлений сет з елементами, які зустрічаються у списку лише один раз:\n{set_of_unique_elements}')

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("\n task 10")
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

str_age_range = {'10-19': [],'20-29': [],'30-39': [],'40-49': []} # назначили змінну для виведення словника
for i in range(len(person_list)): # визначили в якому діапазоні буде працювати цикл (по довжині person_list)
    name = person_list[i][0] # person_list[i][0] - перший елемент у окремому елементі кортежу// 'Alice'
    age = person_list[i][1] # person_list[i][1] - другий елемент у окремому елементі кортежу// 25
    if age >= 10 and age <= 19: # задали віковий діапазон для виконання умови '10-19' 
        str_age_range['10-19'].append(name) # до ключа із віковим діапазоном у випадку співпадінь додавати ім'я
    elif age >= 20 and age <= 29:
        str_age_range['20-29'].append(name)
    elif age >= 30 and age <= 39:
        str_age_range['30-39'].append(name)
    elif age >= 40 and age <= 49:
        str_age_range['40-49'].append(name)
print(str_age_range)