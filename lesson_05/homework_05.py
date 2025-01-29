small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("task 1. Унікальні елементи в списку small_list: ", set(small_list))


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
arithmetic_mean = sum(small_list) / len(small_list)
print("task 2. Cереднє арифметичне всіх елементів у списку small_list: ", arithmetic_mean)


# task 3. Перевірте, чи є в списку big_list дублікати
if len(big_list) == len(set(big_list)):
    print("task 3. В списку big_list немає дублікатів")
else:
    print("task 3. В списку big_list є дублікати")



base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_key = max(add_dict, key=add_dict.get)
print("task 4. Ключ з максимальним значенням у словнику add_dict: ", max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
reversed_dict = {value: key for key, value in base_dict.items()}
print("task 5. Новий словник, в якому ключі та значення замінені місцями; ", reversed_dict) 


# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

for key in base_dict:
    if key in add_dict: 
        sum_dict[key] = f"{base_dict[key]} + {add_dict[key]}"
    else:  
        sum_dict[key] = base_dict[key]

for key in add_dict:
    if key not in sum_dict:
        sum_dict[key] = add_dict[key]

print("task 6. Об'єднайні два словника base_dict та add_dict в новий з об'єднаними значеннями повторюваних ключів", sum_dict)


# task 7. 
line = "Створіть множину всіх символів, які входять у заданий рядок"
char_set = set(line)
print("task 7. Множина всіх символів, які входять у заданий рядок: ", char_set)



# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

diff_sum = sum(set_1 ^ set_2)
print("task 8. Cума елементів двох множин, які не є спільними: ", diff_sum)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
set_task_9 = set(list_1) ^ set(list_2)
print("task 9. Cет, який містить всі елементи з обох списків,  які зустрічаються тільки один раз: ", set_task_9)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_dict = { '10-19': [], '20-29': [], '30-39': [], '40-49': []}

for person in person_list:
    if 10 <= person[1] <= 19:
        person_dict['10-19'].append(person[0])
    elif 20 <= person[1] <= 29:
        person_dict['20-29'].append(person[0])
    elif 30 <= person[1] <= 39:
        person_dict['30-39'].append(person[0])
    elif 40 <= person[1] <= 49:
        person_dict['40-49'].append(person[0])

print(person_dict)
