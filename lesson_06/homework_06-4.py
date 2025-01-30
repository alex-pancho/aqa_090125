# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]
sum = 0

for i in list_of_numbers:
    if i % 2 == 0:
        sum = sum + i

print(f'Sum of even numbers from list', list_of_numbers, 'is:', sum)
