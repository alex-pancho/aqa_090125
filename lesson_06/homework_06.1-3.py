#6.1
user_input = input("Введіть рядок: ")

unique_chars = set(user_input)
result = len(unique_chars) > 10
print(result)

#6.2
while True:
    word = input("Введіть слово, яке містить букву 'h': ")
    
    if 'h' in word.lower():
        print("Дякую! Ви ввели правильне слово.")
        break

    print("Слово не містить 'h', спробуйте ще раз.")
#6.3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lstr2= []
for item in lst1 :
    if type(item) == str:
        lstr2.append(item)
print(lstr2)

