
def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
       які складаються з чисел, розділених комою."""

    for i in string_list:
        try:
            result = sum([int(x) for x in i.split(",")])
        except ValueError:
            result = "Не можу це зробити!"

        return result
