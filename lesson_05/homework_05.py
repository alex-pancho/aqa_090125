small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

uniq_small_list = list(set(small_list))
print(f"{uniq_small_list=}")

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
arithmetic_mean_value = sum(small_list) / len(small_list)
print(f"{arithmetic_mean_value=:.2f}")

# task 3. Перевірте, чи є в списку big_list дублікати
print("Is duplicates:", True if len(big_list) > len(set(big_list)) else False)


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

add_dict_max_key_value = max(add_dict, key=add_dict.get)
print(f"{add_dict_max_key_value=}")

# second variant
max_value = max(add_dict.values())
get_key_with_max_value = [k for k, v in add_dict.items() if v == max_value][0]
print(f"{get_key_with_max_value=}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
new_dict = {f"{v}:{k}" for k,v in add_dict.items()}
print(f"{new_dict=}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
sum_dict = {}
for k, v in add_dict.items():
    for key, value in base_dict.items():
        if k == key:
            sum_dict[k] = f"{v}{value}"
        else:
            sum_dict[k] = v
            sum_dict[key] = value
print(f"{sum_dict=}")

# second variant
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    sum_dict[key] = f"{sum_dict[key]}{value}" if key in sum_dict else value

print(f"{sum_dict=}")

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(f"unique_chars = {set(line)}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_set = sum((set_1 - set_2).union(set_2 - set_1))
print(f"{sum_set=}")

# second variant
print(f"sum_set={sum(set_1 ^ set_2)}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
diff_set1_set2 = set(list_1) ^ set(list_2)
print(list(diff_set1_set2))

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
data = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
for person in person_list:
    name, age = person
    if 10 <= age <= 19:
        data['10-19'].append(name)
    elif 20 <= age <= 29:
        data['20-29'].append(name)
    elif 30 <= age <= 39:
        data['30-39'].append(name)
    else:
        data['40-49'].append(name)
print(data)
