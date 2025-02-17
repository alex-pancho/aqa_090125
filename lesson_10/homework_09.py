#Функція, яка приймає рядок і вираховує Його довжину. Строка повинна бути довжиною від 8 до 20 символів. Виводити помилку для невалідногорядка

def check_string_length (s):
    if not isinstance(s, str):
        return "Помилка! Треба ввести рядок"
    length = len(s)
    if length < 8:
        return "Помилка! Мінімальна кількість символів - 8"
    if length > 20:
        return "Помилка! Максимальна кількість символів - 20"
    else:
        return "Все ок! Довжина рядка від 8 до 20 символів"
    
#Валідація емейлу
import re
def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))  

# Функція, яка формує новий list,
# який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]