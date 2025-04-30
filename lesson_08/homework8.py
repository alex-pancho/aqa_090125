def calculate_sum(number_string):
    try:
        numbers = number_string.split(',')
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

# Вхідний масив
array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Обробка кожного елементу масиву
for item in array:
    result = calculate_sum(item)
    print(result)