small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("*"*30+"task 1"+"*"*30)
unic_small_list = set(small_list)
print(f"Унікальні символи в small_list: {unic_small_list}")


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("*"*30+"task 2"+"*"*30)
average_small_list = sum(small_list)/len(small_list)
print(f"Середнє арифметичне всіх елементів у списку small_list: {average_small_list}")


# task 3. Перевірте, чи є в списку big_list дублікати
print("*"*30+"task 3"+"*"*30)
if len(big_list)>len(set(big_list)):
    print(f"Так, в списку big_list є дублікати")
else:
    print(f"Ні, в списку big_list немає дублікатів")

          
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("*"*30+"task 4"+"*"*30)
max_key = max(add_dict, key=add_dict.get)
print(f"Ключ з максимальним значенням у словнику add_dict: {max_key}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("*"*30+"task 5"+"*"*30)
swapped_dict = {value: key for key, value in add_dict.items()}
print(f"Зворотній словник:\n{swapped_dict}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("*"*30+"task 6"+"*"*30)
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    sum_dict[key] = str(sum_dict[key]) + str(value) if key in sum_dict  else value
print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print("*"*30+"task 7"+"*"*30)
new_set = set(line)
print(f"Множина всіх символів в рядку:\n{new_set}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("*"*30+"task 8"+"*"*30)
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_sets = sum(set_1 ^ set_2)
print(f"Cума елементів двох множин, які не є спільними: {sum_sets}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("*"*30+"task 9"+"*"*30)
list_1 = [6, 2, 46, 5, 9, 10, 0, 3]
list_2 = [x+1 for x in list_1] 
unic_set = set(list_1) ^ set(list_2)
print(f"Сет, який містить всі елементи з обох списків,  які зустрічаються тільки один раз:\n{unic_set}")

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("*"*30+"task 10"+"*"*30)
age_groups = {}
for name, age in person_list:
    key = f"{age//10*10}-{age//10*10+9}"
    age_groups.setdefault(key, []).append(name)
print(age_groups)