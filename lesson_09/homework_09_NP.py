def get_even_numbers(lst):
    """Повертає список парних чисел зі вхідного списку."""
    even_numbers = []
    
    for num in lst:
        if isinstance(num, (int, float)) and num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers

def clean_dictionary(data):
    """Замінює null-подібні значення на 0 у словнику."""
    for key in ['sum', 'count']:
        if str(data.get(key)).lower() in ['null', 'none', 'nan']:
            data[key] = 0
    
    return data

def is_palindrome(word):
    """Перевірка, чи є слово паліндромом."""
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]