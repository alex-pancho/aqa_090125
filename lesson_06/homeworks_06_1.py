# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. 
# Строку отримати за допомогою функції input()

input_string = input("Введіть строку: ")
unique_chars = set(input_string)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)
