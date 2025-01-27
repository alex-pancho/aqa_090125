small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

small_list_uniqe = set(small_list)
print (f"Uniqe values in list", list(small_list_uniqe))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

small_list_arithmetic_mean = sum(small_list)/len(small_list)
print(f"Arithmetic mean of all elements in the list =", small_list_arithmetic_mean)

# task 3. Перевірте, чи є в списку big_list дублікати

big_list_len = len(big_list)
big_list_to_set_len = len(set(big_list))

if big_list_len != big_list_to_set_len:
    print("Duplicates found")
else:
    print("No duplicates found")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_add_dict_value = max(add_dict, key=lambda x: len(x))
print(f"Longest key in dict:", max_add_dict_value)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

keys = base_dict.keys()
values = base_dict.values()
reversed_dict = dict(zip(values, keys))
print(reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = base_dict.copy()
for key, value in add_dict.items():
    sum_dict[key] = str(sum_dict[key]) + str(value) if key in sum_dict else value

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_from_string = set(line)
print(set_from_string)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

logical_symmetric_difference = set_1 ^ set_2
logical_symmetric_difference_sum = sum(logical_symmetric_difference)
print ("The sum of the elements of two sets that are not common =", logical_symmetric_difference_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_01 = [1, 2, 3, 4]
list_02 = [3, 4, 5, 6]
list_01_to_set = set(list_01)
list_02_to_set = set(list_02)
diff_set1_set2 = list_01_to_set ^ list_02_to_set
print (list(diff_set1_set2))

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_ranges = {}

for name, age in person_list:
    age_range = f"{age // 10 * 10}-{age // 10 * 10 + 9}"
    if age_range not in age_ranges:
        age_ranges[age_range] = []
    age_ranges[age_range].append(name)
print(age_ranges)

