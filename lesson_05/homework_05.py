small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_elements = list(set(small_list))
print("Унікальні елементи:", unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

avg_sum = sum(small_list) / len(small_list)
print("Середнє арифметичне всіх елементів у списку small_list:",avg_sum)

# task 3. Перевірте, чи є в списку big_list дублікати

check_for_duplicates = len(big_list) == len(set(big_list))
if check_for_duplicates is True:
    print("Дублікатів немає")
else:
    print("Є дублікати")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

add_dict_all_values = add_dict.values()
max_value = max(add_dict_all_values)
print("Максимальне значення:",max_value)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key in base_dict.keys() | add_dict.keys():
    if key in base_dict and key in add_dict:
        sum_dict[key] = str(base_dict[key]) + str(add_dict[key])
    elif key in base_dict:
        sum_dict[key] = base_dict[key]
    else:
        sum_dict[key] = add_dict[key]
print(sum_dict)
# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

set_of_all_symbols = set(line)
print(set_of_all_symbols)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_3 = set_1 ^ set_2
print(set_3)
summ_of_elements = sum(set_3)
print('Сума елементів двох множин, які не є спільними:', summ_of_elements)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
list_1_to_set = set(list_1)
list_2_to_set = set(list_2)
combined_set = list_1_to_set ^ list_2_to_set
print(combined_set)


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

age_group = {}

for name, age in person_list:
    start_age = (age // 10) * 10
    end_age = start_age + 9
    age_range = f"{start_age}-{end_age}"
    age_group.setdefault(age_range, []).append(name)

print(age_group)


