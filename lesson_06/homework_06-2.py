# Напишіть цикл, який буде вимагати від користувача ввести слово, 
# в якому є літера "h" (враховуються як великі так і маленькі). 
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

word_from_input = ""
expected_input_lover = "h"
expected_input_upper = "H"

while (expected_input_lover not in word_from_input) and (expected_input_upper not in word_from_input):
    word_from_input =  input('Enter string that contains "h" or "H" letter:')

