small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unic_elements = list(set(small_list))

sorted_unic_elements = sorted(unic_elements, reverse = True)
print ("Unic values from small_list and big_list are :", sorted_unic_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

small_list_arithmetic_mean = sum(small_list) / len(small_list)
print (f"Arithmetic mean of values in the small_list are: {small_list_arithmetic_mean:.2f}")

# task 3. Перевірте, чи є в списку big_list дублікати

big_list_without_dublicates = list(set(big_list))
duplicates_presence = len(big_list) != len(big_list_without_dublicates)
print (f"Does big_list contains duplicates of the values - {duplicates_presence}")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_value = max(add_dict.values())
print (f"Max value in the add_dict dictionary is {max_value}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

my_new_dict = {'Ukraine' : 'contry', 'Europe' : 'continent', '123' : 'size' }
print (f"Newlly created dictionary is {my_new_dict}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

same_keys = set(base_dict.keys()).intersection(set(add_dict.keys()))
sum_dict = {**base_dict, **add_dict}
sum_dict.update({key: f"{base_dict[key]}-{add_dict[key]}" for key in same_keys})
print(f"United base_dict and add_dict sets : {sum_dict}")

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
separated_symbols = set(line)
print("Task 7 answer:", separated_symbols)

# task 8. Обчисліть суму елементів двох множин, які не є спільними

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
diferent_value = sum(set_1.symmetric_difference(set_2))
print("Total of values which are different in the set_1 and set_2 =", diferent_value)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

custom_list_1 = [1, 2, 3, 4, 5]
custom_list_2 = [4, 6, 5, 10]
custom_set_1 = set(custom_list_1)
custom_set_2 = set(custom_list_2)
unic_values_from_lists = custom_set_1^custom_set_2  
print("Unic values from are custom_list_1 and custom_list_2  are ", unic_values_from_lists)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
person_dictionary = dict(person_list)
new_person_dictionary_sorted = dict(sorted(person_dictionary.items(), key=lambda item: item[1]))
new_key_sorted = list(new_person_dictionary_sorted.values())
new_values_sorted = list(new_person_dictionary_sorted.keys())
ranges = {}
for age in range(0, len(new_key_sorted) - 1, 2):
    range_key = f'{new_key_sorted[age]}-{new_key_sorted[age + 1]}'
    ranges[range_key] = [new_values_sorted[name] for name in range(age, age + 2)]
print("Answer for task №10 :",ranges)