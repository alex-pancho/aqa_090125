small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

# task 3. Перевірте, чи є в списку big_list дублікати
unique_symbols_at_small_list = set(small_list)
arithmetic_mean_at_small_list = sum(small_list)/len(small_list)
dublicates_of_big_list = len(big_list) !=len(set(big_list))

print("Список унікальних елементів",unique_symbols_at_small_list)
print("Середнє арифметичне всіх елементів",arithmetic_mean_at_small_list)
print("Наявність дублікатів",dublicates_of_big_list)


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict, key=add_dict.get)
print(f"Максимальним значенням у словнику add_dict = {max_key}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
swapped_dict = {value: key for key,value in add_dict.items()}
print(f"Зворотній словник - {swapped_dict}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {key: (str(base_dict[key]) + str(add_dict[key]) if key in base_dict and key in add_dict
                  else base_dict.get(key, add_dict.get(key)))
            for key in base_dict.keys() | add_dict.keys()}
print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_set = set(line)
print(f"Множина всіх символів -{new_set}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_sets = sum(set_1 ^ set_2)
print(f"Сума неспільних двох множин - {sum_sets}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [3,2,55,1,10,7.5]
list_2 = [4,3,44,2,9,3.14]
unic_set = set(list_1) ^ set(list_2)
print(f"Унікальний список із двох списків - {unic_set}")

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_groups = {}
for name, age in person_list:
    key = f"{age//10*10}-{age//10*10+9}"
    age_groups.setdefault(key,[]).append(name)
print(dict(sorted(age_groups.items())))