small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_values_list = list(set(small_list))
print(unique_values_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average_value = sum(small_list) / len(small_list)
print(average_value)

# task 3. Перевірте, чи є в списку big_list дублікати

check_duplicates = len(big_list) != len(set(big_list))
print(check_duplicates)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict, key=add_dict.get)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

reversed_dict = dict((value, key) for key, value in base_dict.items())
print(reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

for key in base_dict:
    sum_dict[key] = base_dict[key]

for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

unique_chars = set(line)
print(unique_chars)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

exclusive_elements = (set_1 - set_2) | (set_2 - set_1)
sum_exclusive = sum(exclusive_elements)
print(sum_exclusive)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

set_1 = set(list_1)
set_2 = set(list_2)

unique_elements = (set_1 - set_2) | (set_2 - set_1)

print(unique_elements)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_groups = {}

for name, age in person_list:
    if 10 <= age < 20:
        age_range = '10-19'
    elif 20 <= age < 30:
        age_range = '20-29'
    elif 30 <= age < 40:
        age_range = '30-39'
    elif 40 <= age < 50:
        age_range = '40-49'
    else:
        continue

    if age_range not in age_groups:
        age_groups[age_range] = []
    age_groups[age_range].append(name)

print(age_groups)
