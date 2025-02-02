# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

#Первый варант
string = input("Введи свою фразу")
unic_symbols = len(set(string))
if unic_symbols>10:
    print("True")
else:
    print("False")

#Второй варант
string = input("Уважаемый,напишите свою фразу")
unic_symbols = len(set(string))
print(unic_symbols>10)
