# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    while True:
        result = number * multiplier
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum(a, b):
    """Calculate sum of two digits."""
    return a + b

print(f'Sum of numbers is:', sum(53, 57))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def get_average(nums:list):
    """Calculate avarage of the list of numbers."""
    sum_num = 0
    for t in nums:
        sum_num = sum_num + t           
    avg = sum_num / len(nums)
    return avg

print("The average is", get_average([18, 2, 65, 25, 3, 34, 8, 83, 74, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(string):
    """Reverse string and returns string."""
    reversed_string = ''.join(list(reversed(string)))
    return reversed_string

print (reverse_string("String to reverse!"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    """Find and return the longest word in the list."""
    return max(words, key=len)

word_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(longest_word(word_list))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2) 

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

def albbum_capacity_needed (page_capacity, photos_amount): 
    """Calculate album capacity needed."""
    pages_required = photos_amount/page_capacity
    return pages_required

pages_needed = albbum_capacity_needed(page_capacity = 8, photos_amount = 232)
print (f'Igor will need {pages_needed} pages of the album.')

# task 8
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def price_of_the_item (monthly_payment, payment_time):
    """Calculate price of the item based on monthly payment amount and payment time."""
    price = monthly_payment * payment_time
    return price

print (f'Computer price is {price_of_the_item(1179, 18)}')

# task 9
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

def fuel_per_treep(treep_distance, fuel_consumption_per_100):
    """Calculate how many fuel is needed for the trip based on distance and consumption."""
    fuel_per_treep_needed = (treep_distance/100) * fuel_consumption_per_100
    return fuel_per_treep_needed

def min_fuel_refill(treep_distance, fuel_consumption_per_100, tank_capacity):
    """Calculate how many fuel refuil are needed for the trip based on distance, capacity and consumption."""
    fuel_per_trip_required = fuel_per_treep(treep_distance, fuel_consumption_per_100)
    min_fuel_refill = fuel_per_trip_required /tank_capacity
    return min_fuel_refill

print (f'The trip will require {fuel_per_treep(1600, 9)} liters of fuel. '
    f'Minimum {min_fuel_refill(1600, 9, 48)} fuel refill per treep needed.')

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# Перевірте, чи є в списку big_list дублікати

def check_list_for_duplicates (big_list):
    """Check the list for duplicates."""
    big_list_len = len(big_list)
    big_list_to_set_len = len(set(big_list))
    if big_list_len != big_list_to_set_len:
        return ("Duplicates found")
    else:
        return ("No duplicates found")

print(check_list_for_duplicates([3, 5, -2, -1, -3, 0, 1, 4, 5, 2]))
