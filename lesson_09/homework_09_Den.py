
def count_vowels(input_string: str):
    """Функция подсчета гласных букв в строке"""
    vowels_list = ['a', 'e', 'o', 'y', 'i', 'u']
    vowels_counts = {}
    for letter in input_string.lower():
        if letter in vowels_list:
            if letter in vowels_counts:
               vowels_counts[letter] += 1
            else:
                vowels_counts[letter] = 1
    return vowels_counts
print(count_vowels("Hello, world!"))  # {'e': 1, 'o': 2}
print(count_vowels("Python is awesome!"))  # {'o': 2, 'i': 1, 'a': 1, 'e': 2}
print(count_vowels("AEIOUYaeiouy"))  # {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2, 'y': 2}
print(count_vowels("bcdfg"))  # {}




def compare_grades(grades_1: dict, grades_2: dict):
    """Функция сравнения оценок студентов"""
    result = {}
    all_students = set(grades_1) | set(grades_2)
    for student in all_students:
        if student in grades_1 and student in grades_2:
            result[student] = grades_1[student] - grades_2[student]
        elif student in grades_1 and student not in grades_2:
            result[student] = grades_1[student]
        elif student in grades_2 and student not in grades_1:
            result[student] = grades_2[student]

    return result
print(compare_grades(
    {'Анна': 90, 'Ваня': 89},
    {'Анна': 85, 'Ваня': 87}
))

print(compare_grades(
    {'Анна': 90, 'Ваня': 89},
    {'Анна': 90}
))

print(compare_grades(
    {'Анна': 90},
    {'Анна': 85, 'Ваня': 87}
))



def sum_positive_numbers(numbers: list):
    """Возвращает сумму всех положительных чисел в списке"""
    if not isinstance(numbers, list):
        raise ValueError("Функция принимает в качестве аргумента только список")

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise ValueError("Список должен содержать исключительно числа")
    total = sum(number for number in numbers if number > 0)

    return total
if __name__...
    print(sum_positive_numbers([1, -2, 3, 4, -5]))
print(sum_positive_numbers([-1, -2, -3]))
print(sum_positive_numbers([10, 20, 30]))
print(sum_positive_numbers([]))
