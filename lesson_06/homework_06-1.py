# Порахувати кількість унікальних символів в строці. 
# Якщо їх більше 10 - вивести в консоль True, інакше - False. 
# Строку отримати за допомогою функції input()

some_string =  input("Enter your string:")

print("Does your input contain more than 10 unique symbols:", end=" ")

if len(set(some_string)) > 10:
    print("True")
else:
    print("False")


