# LMS 6_1
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
user_string = input("Please enter string values: ")
unique_symbols_of_str = set(user_string)

if len(unique_symbols_of_str) > 10:
    print(True)

else:
    print(False)

# LMS 6_2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    user_word = input("Enter a word that contains the letter 'H' or 'h': ")
    
    if 'h' in user_word.lower():
        print("CONGRATULATIONS!!!\n You enter correct word!!! ")
        break
    
    else:
        print("Pease try one more time.")

# LMS 6_3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який свормує новий 
# list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [str_value for str_value in lst1 if type(str_value) is str] 
print("Values from \'lst1\' with type string for \'lst2\' will be :", lst2)

# LMS 6_4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_numeric = [ -1, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]
even_numbers_total = 0
for even_numbers in list_numeric:
    if even_numbers % 2 == 0:
        even_numbers_total += even_numbers
print("Total of even numbers from list is :", even_numbers_total)
