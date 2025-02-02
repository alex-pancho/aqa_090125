small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("\n", "task 1")
unicElements = set(small_list)
print(f"Якщо зі списку {small_list} вивести усі унікальні елементи, то ми отримаємо: {unicElements}")

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("\n", "task 2")
sumSmallList = sum(small_list)
countSmallList = len(small_list)
arithmeticSum = sumSmallList/countSmallList
print(f"Середнє арифметичне всіх елементів у списку {small_list} дорівнює {arithmeticSum:.3}")

# task 3. Перевірте, чи є в списку big_list дублікати
print("\n", "task 3")
unicElements = set(big_list)
if len(big_list) != len(unicElements):
    print("Так, у списку є дублікати")
else:
    print("Ні, у списку немає дублікатів")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("\n", "task 4")
maxKey = max(add_dict, key=add_dict.get)
print("Ключ з максимальним значенням у словнику:", maxKey)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("\n", "task 5")
allKeys = add_dict.keys()
allValues = add_dict.values()
newDict = dict(zip(allValues, allKeys))
print(f"Якщо у словнику {add_dict} поміняти місцями ключі та значення, то вийде новий словник: {newDict}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("\n", "task 6")
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print(f"Якщо об'єднати словники {base_dict} i {add_dict}, то вийде: {sum_dict}")

# task 7.
print("\n", "task 7")
line = "Створіть множину всіх символів, які входять у заданий рядок"
mySet = set(line)
print(f"Mножинa всіх символів у рядку: {mySet}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("\n", "task 8")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
setDifference = set_1.symmetric_difference(set_2)
sumElements = sum(setDifference)
print(f"Якщо обрати елементи, які не будуть повторюватись у обох множин, то отримаємо: {setDifference}. "
      f"Їхня сума дорівнює: {sumElements}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків, які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("\n", "task 9")
myList1 = ['a', 'b', 'c', 'd', 'e']
myList2 = ['c', 'd', 'e', 'f', 'g']
mySet1 = set(myList1)
mySet2 = set(myList2)
myNewList = list(mySet1.symmetric_difference(mySet2))
print(f"Маємо два списки: {myList1} та {myList2}. "
      f"Якщо вивести всі елементи з обох списків, які зустрічаються тільки один раз, то отримаємо: {myNewList}")

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("\n", "task 10")
ageGroups = {}
for name, age in person_list:
    key = f"{age//10*10}-{age//10*10+9}"
    ageGroups.setdefault(key, []).append(name)
print(f"Якщо перетворити список кортежів {person_list} на словник з віковими діапазонами, то отримаємо {ageGroups}")
