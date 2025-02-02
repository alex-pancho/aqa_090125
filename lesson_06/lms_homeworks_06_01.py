# LMS 6_1
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
user_string = input("Please enter string values: ")
unique_symbols_of_str = set(user_string)
if len(unique_symbols_of_str) > 10:
    print(True)
else:
    print(False)