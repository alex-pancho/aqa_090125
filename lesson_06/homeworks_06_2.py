# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі). 
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    word = input("Введіть слово, в якому є літера 'h': ")
    
    if 'h' in word.lower():
        print("Ви ввели правильне слово.")
        break
    else:
        print("Слово не містить літеру 'h'. Введіть слово, в якому є літера 'h':")
