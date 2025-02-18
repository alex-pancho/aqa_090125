def longest_word_in_list(list_of_words:list):
    """Finds the longest word in list"""
    for el in list_of_words:
        if not isinstance(el, str):
            raise TypeError("Помилка введених даних")
    if not isinstance(list_of_words, list):
        raise TypeError("Помилка введених даних")
    if list_of_words == []:
        raise TypeError("Помилка введених даних")
    word = max(list_of_words, key = len)
    return(word)


def solution_for_diff_in_dicts(grades1: dict, grades2: dict):
    """Compares grades in dict and returns difference of values"""
    if not isinstance(grades1, dict):
        raise TypeError("Помилка введених даних")
    if not isinstance(grades2, dict):
        raise TypeError("Помилка введених даних")
    for key in grades1:
        # Перевіряємо, чи присутній ключ в обох словниках
        if key not in grades2:
            raise AttributeError("Помилка введених даних")
    for key in grades2:
        if key not in grades1:
            raise AttributeError("Помилка введених даних")
    x = {}
    for key in set(grades1.keys()) and set(grades2.keys()):
        x[key] = grades1.get(key, 0) - grades2.get(key, 0)
    return x


# Значення аргументів за замовчуванням: аргументи multiplier і end_with ініціалізуються значенням None, щоб дозволити перевірку їх наявності.
def multiplication_table(multiplier: int = None, end_with: int = None):
    """Prints the multiplication table for a given number and stops at the specified number"""
    if multiplier is None or end_with is None:
        raise ValueError("Помилка введених даних")
    if not isinstance(multiplier, int):
        raise TypeError("Помилка введених даних")
    if not isinstance(end_with, int):
        raise TypeError("Помилка введених даних")
    start_from = 1
    table = []
    while start_from <= end_with:
        result = start_from * multiplier
        table.append(f"{start_from} x {multiplier} = {result}")
        start_from += 1
    return "\n".join(table)