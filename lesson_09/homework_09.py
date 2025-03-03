def summ_of_number_items(number):
    """функція, яка знаходить суму всіх цифр натурального числа, яке вводить користувач"""
    counter = []
    result = 0
    for i in number:
        counter.append(i)
        try:
            result = sum([int (i) for i in counter])
        except ValueError:
            result = f"Помилка: {number}. Для знаходження суми потрібно, щоб усі введені данні були числами."
        except TypeError:
            result = f"Помилка: {number}. Серед введених даних є некоректний тип."

    return result

if __name__ == '__main__':
    print(summ_of_number_items([1,2,3,4,5]))
    print(summ_of_number_items([1,2,'t',4,5]))
    print(summ_of_number_items([]))
    print(summ_of_number_items([1,2,sum,4,5]))


def find_substring(value1, value2):
    """функція, яка приймає два рядки та повертає індекс першого входження другого рядка у перший рядок.
    Якщо другий рядок не є підрядком першого рядка повертає -1 """
    try:
        if value2 in value1:
            result =  tuple(value1).index(tuple(value2)[0])
        else:
            result = f"Рядок: {value2} не входить в рядок: {value1}."
    except TypeError:
        result = f"Помилка: {value2} не є рядком"
    except IndexError:
        result = f"Помилка: {value2} не містить жодне значення"

    return result

if __name__ == '__main__':
    str1 = "функція, яка приймає два рядки"
    str2 = "яка"
    print(find_substring(str1, str2))
    print(find_substring(str1, "два"))
    print(find_substring(str1, "dva"))
    print(find_substring(str1, 3))
    print(find_substring(str1, ""))

def multiplication_table(number):
    """функція, яка надрукує табличку множення на задане число,
    але лише до максимального значення для добутку - 25"""
    multiplier = 1
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
    return result

if __name__ == '__main__':
    multiplication_table(3)
    multiplication_table(26)

def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк, які складаються з чисел, розділених комою."""
    result = []
    for i in string_list:
        try:
            result.append(sum([int(x) for x in i.split(",")]))
        except ValueError as e:
            result.append("Не можу це зробити!")

    return result

if __name__ == '__main__':
    print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))
    print(sum_numbers_in_list(["1,2,3,4", "7"]))
    print(sum_numbers_in_list([]))


def is_duplicates(list_of_values):
        """ функція, яка перевіряє чи є в списку дублікати """
        return len(list_of_values) != len(set(list_of_values))
if __name__ == '__main__':
    print(is_duplicates([1,2,3,4,5]))
    print(is_duplicates([1,2,5,4,5]))
    print(is_duplicates(['t', 'a', 'b', 'c', 'T']))
    print(is_duplicates(['t', 'a', 'b', 'c', 't']))
