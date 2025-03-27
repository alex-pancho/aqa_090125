def multiplication_table(number):
    multiplier = 1
    while multiplier <= number:
        result = number * multiplier
        if  result > "25":
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multi += 1

multiplication_table(3)
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
result = sum_two_numbers(5, 3)
print(result)



# task 3
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(result)


# task 4
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)


# task 5
words = ["apple", "banana", "kiwi", "strawberry", "blueberry"]
longest = find_longest_word(words)
print(longest)


# task 6
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

#task 7
number = input("Введіть натуральне число: ")
sum_of_digits = 0

for digit in number:
    sum_of_digits += int(digit)

print(f"Сума цифр числа {number}: {sum_of_digits}")

#task 8
total_sum = 0

while True:
    number = int(input("Введіть число (або 0 для завершення): "))
    if number == 0:
        break
    total_sum += number

print(f"Сума всіх введених чисел: {total_sum}")

#task 9
mport random

secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5

print("Вгадайте число від 1 до 20 за 5 спроб!")

for attempt in range(max_guesses):
    guess = int(input("Ваше припущення: "))
    guesses += 1

    if guess < secret_number:
        print("Занадто мале число.")
    elif guess > secret_number:
        print("Занадто велике число.")
    else:
        print(f"Вітаємо! Ви вгадали число {secret_number} за {guesses} спроб.")
        break
else:
    print(f"На жаль, ви не вгадали. Загадане число було {secret_number}.")

    #tasak 10
    fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)