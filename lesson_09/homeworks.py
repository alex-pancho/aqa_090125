#Функції для тестування

#Функія №1 
def list_of_strings(lst: list) -> list:
    """Функція приймає список і повертає список тільки зі строкових значень"""
    if lst == []:
        raise ValueError("Список пустий!")
    
    if not isinstance(lst, list):
        return "Введіть список!"
    
    lst_str = [elem for elem in lst if isinstance(elem, str)]

    if not lst_str:
        return "В списку немає строкових значень!"
    
    return lst_str
    


#Функія №2 
def reversed_dict(base_dict: dict) -> dict:
    """Функція приймає словник і повертає його копію, де ключі і значення поміняні місцями"""

    if not isinstance(base_dict, dict):
        return "Введіть словник!"
    if base_dict == {}:
        return "Словник пустий!"
    try:
        rev_dict = {value: key for key, value in base_dict.items()}
    except TypeError:
        return "Некоректний тип ключа"
    
    return rev_dict



#Функія №3
def average_of_list(lst: list) -> float:
    """Функція приймає список чисел і повертає середнє арифметичне"""
    if not lst:  
        raise ValueError("Список порожній! Не можна обчислити середнє.")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise TypeError("Список повинен містити тільки числа!")
    
    if not isinstance(lst, list):
        raise TypeError("Введіть список!")
    
    ar_average = sum(lst) / len(lst)
    return ar_average


#Функія №4
def calculate_sum_from_file(filename):
        
    numbers = []
    try:
        with open(filename, 'r') as file:
            content = file.read()

        word = content.split()

        for number in word:
            if number.isnumeric():
                numbers.append(int(number))
    except FileNotFoundError:
        return ("File not found")
    except ValueError:
        return("Invalid data in the file")
         

    numbers_sum = sum(numbers)
    return numbers_sum

