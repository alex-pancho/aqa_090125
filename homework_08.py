# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.


def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк, які складаються з чисел, розділених комою."""

    if string_list == []:
         raise ValueError ('Список порожній!')
    if not isinstance(string_list, list):
         raise ValueError ('Введіть список!')
    
    result = []
    
    try:
        for string in string_list:
            try: 
                numbers = [int(number) for number in string.split(',')]
                result.append(sum(numbers))
            except ValueError:
                result.append('Не можу це зробити! ValueError')
            except AttributeError:
                result.append('Не можу це зробити! AttributeError')
    except TypeError:
            result.append('Не можу це зробити! TypeError')    
        

    return result

print(sum_numbers_in_list(['1,2,3' , '4,0,6', 'asas7,8,9']))
print(sum_numbers_in_list(['1,2,3' , '4/0,6', 'asas7,8,9']))
print(sum_numbers_in_list(['1,2,3' , '4/0,6', 'asas7,8,9', 7]))        
print(sum_numbers_in_list('21'))
print(sum_numbers_in_list(3))
print(sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}]))
print(sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50", sum, min(1,2)]))
print(sum_numbers_in_list((21)))
print(sum_numbers_in_list([]))