# Порахувати кількість унікальних символів в строці. 
# Якщо їх більше 10 - вивести в консоль True, інакше - False. 
# Строку отримати за допомогою функції input() 

numbers = input("Введіть числа через пробіл: ").split()
print(numbers)
if len(set(numbers)) > 10:
    print(True)
else: 
    print(False)