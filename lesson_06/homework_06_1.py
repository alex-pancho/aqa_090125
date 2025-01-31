#Порахувати кількість унікальних символів в строці. 
#Якщо їх більше 10 - вивести в консоль True, інакше - False. 
#Строку отримати за допомогою функції input()
user_input = input('Enter a string: ')
unique_chars = set(user_input)
print(len(unique_chars) > 10)
