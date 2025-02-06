
def hello_student():
    print("Hello my student")

hello_student()

def hello_user(name):
    print(f"Hello {name}")

# hello_user("Denys")
# hello_user("Olga")
# hello_user("Leonyd")
user_names = ["Denys", "Olga", "Leonyd"]
user_ann = "Ann"
for user in user_names:
    
    hello_user(user)
    hello_user(user_ann)

def sum(a, b):
    return a + b
c = sum(1, 1)
print(c)
# print(sum(1, 1))
print(abs(-10))
print(all([[]]))
print("sum:", callable(sum))
print("c:", callable(c))
print(chr(1111))

def is_even(n):
    return n % 3 == 0

# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Використання filter для отримання парних чисел
filtered_numbers = filter(is_even, numbers)
print(filtered_numbers)
# Перетворення результату в список
even_numbers = list(filtered_numbers)

print(even_numbers)


filtered_numbers = set(filter(is_even, numbers))
print(filtered_numbers)
# help(print)
print(isinstance(even_numbers, dict))


base_numbers = [2, 3, 4, 5, 10]
powers = [1, 2, 3, 4, 5]
# print(pow(base_numbers[0], powers[0]))
numbers_powers = list(map(sum, base_numbers, powers))
print(numbers_powers)
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))
some_dict = {b:a for a, b in zip(list1, list2) }
print(some_dict)
list2 = [4, 5, 6]
sums = [a + b for a, b in zip(list1, list2)]
print(sums)

