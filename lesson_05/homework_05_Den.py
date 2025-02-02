small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_elements_from_small_list = list(set(small_list))
print(unique_elements_from_small_list, "\n")

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
elements_quantity_small_list = len(small_list)
print(elements_quantity_small_list)
arithmetic_mean_from_small_list = ((small_list[0] + small_list[1] + small_list[2] + small_list[3] + small_list[4] + small_list[5] + small_list[6])) / elements_quantity_small_list
print(arithmetic_mean_from_small_list, "\n")

# task 3. Перевірте, чи є в списку big_list дублікати
set_from_big_list = set(big_list)
check_list = big_list
print("Checked list contains duplicates: ", len(check_list) > len(set_from_big_list), "\n")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
key_with_biges_value = list(add_dict.keys())[list(add_dict.values()).index(sorted(add_dict.values())[-1])]
print(key_with_biges_value, "\n")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {}
list_of_value_base_dict = list(base_dict.values())
list_of_key_base_dict = list(base_dict.keys())
new_dict = dict(zip(list_of_value_base_dict, list_of_key_base_dict))
print(new_dict, "\n")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
# Я знаю что в словорях есть одинаковые ключи - size. Я хочу сразу перевести Их оба значания в сроку,
# сложить в единую строку и поместить в значения ключа первого словоря. Потом буду просто обновлять одлин словарь другим
base_dict_size_value = str(base_dict['size'])
add_dict_size_value = str(add_dict['size'])
new_size_value = base_dict_size_value + add_dict_size_value
base_dict['size'] = new_size_value
sum_dict.update(add_dict)
sum_dict.update(base_dict)
print(sum_dict, "\n")

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_from_line = set(line)
print(set_from_line, "\n")
# Может я не правильно понял задание, но как можно создать множество из всех символов, если символы повторяються, а множество
# есть уникальной последовательностью? Другого решения я не вижу - для ВСЕХ сымволов в множество будут все равно всложены
# либо списки либо картежи

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_elements_from_current_sets = set_1 ^ set_2
print(sum(unique_elements_from_current_sets), "\n")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_x = [number for number in range(0, 80) if number % 4 == 0]
list_y = [number for number in range(20, 100) if number % 3 == 0]
set_of_union_lists_values = set(list_x) | set(list_y)
print(list_x, "\n", list_y, "\n", set_of_union_lists_values, "\n")

# -------------------------------------------------------------------------

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_dict = {'10-19': [name for name, age in person_list if 10 <= age <= 19],
             '20-29': [name for name ,age in person_list if 20 <= age <= 29],
             '30-39': [name for name, age in person_list if 30 <= age <= 39],
             '40-49': [name for name, age in person_list if 40 <= age <= 49]
             }
print(person_dict)










