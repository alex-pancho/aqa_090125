#task 1
def average_number(numbers: list[int]) -> float: 
    """
    Функція, яка розрахує середнє арифметичне списку чисел.
    """
    return sum(numbers) / len(numbers) 

# task 2
def longest_word(words: list[str]) -> str:
    """ 
    Функція, яка приймає список слів та повертає найдовше слово у списку.
    """
    return max(words, key=len)

# task 3
def calculate_total_cost(order: list):
    """ 
    Функція обчислює загальну вартість замовлення.
    """
    total_cost = 0

    for item in order:
        name, quantity, price = item
        total_cost = total_cost + (quantity * price)
    return total_cost

#task 4
def reverse_string(s):
    """  
    Функція, яка приймає рядок та повертає його у зворотному порядку.
    """
    return s[::-1]

#task 5
def is_even(number: int) -> bool:
    """
    Функція перевіряє, чи є число парним.
    """
    return number % 2 == 0

if __name__ == "__main__":

# Перевірка функцій 
# task 1
    nums = [5, 6, 7]
    result = average_number(nums)

    print(f"Середнє арифметичне списку {nums} дорівнює {result}")

# task 2
    word_list = ["New York", "Los Angeles", "Kyiv", "Porto"]

    print(f"Найдовше слово у списку: {longest_word(word_list)}")

# task 3
    order_list = [
        ("Піца велика", 4, 274),
        ("Піца середня", 2, 218),
        ("Сік", 4, 35),
        ("Торт", 1, 350),
        ("Вода", 3, 21)
    ]

    total_price = calculate_total_cost(order_list)

    print(f"Загальна вартість замовлення: {total_price} грн")

# task 4
    text = "Прочитай цей рядок у зворотному порядку!"
    reverse_text = reverse_string(text)

    print(f"Оригінальний рядок: {text}")
    print(f"Реверсований рядок: {reverse_text}")

# task 5
    check_num = is_even(54)

    print(f"Парне число? - {check_num}")