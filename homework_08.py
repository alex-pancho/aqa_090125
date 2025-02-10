# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

def sum_of_numbers(string_list=[]):
    if not string_list: 
        return "Список порожній"  
    if not isinstance(string_list, list):
        return "Not a list"      
    results = []
    try: 
        for item in string_list:
            if not isinstance(item, str):
                results.append("Не можу це зробити! Not a string")
                continue
            if item == "":
                results.append("Не можу це зробити! Empty string")
                continue
            try:
                numbers = map(int, item.split(","))
                results.append(sum(numbers)) 
            except ValueError: 
                results.append("Не можу це зробити! ValueError")
            except AttributeError:
                results.append("Не можу це зробити! AttributeError")
            except Exception as e:
                results.append(f"Не можу це зробити! Unknown Error: {str(e)}")
        return results  
    except TypeError:
        print("Не можу це зробити! TypeError")

print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", 4+5, "qwerty1,2,3"]))
print(sum_of_numbers((21)))
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", 7]))
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", (3, 3, 6, 4), "1,2,3"]))
print(sum_of_numbers())
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", "", "qwerty1,2,3"]))
print(sum_of_numbers([]))
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}]))
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", sum, min(6,8)]))
print(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", (3, 3, 6, 4), "1,2,3"]))
print(sum_of_numbers(3))
print(sum_of_numbers(["1,2,3,4,7"]))