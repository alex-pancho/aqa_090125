#Напишіть цикл, який буде вимагати від користувача ввести слово, 
# #в якому є літера "h" (враховуються як великі так і маленькі). 
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
user_input = input("Enter a word: ")
while "h" not in user_input or "H" not in user_input:
    user_input = input("Enter a word with the letter 'h' or 'H': ")
print("The word contains the letter 'h' or 'H'.")

