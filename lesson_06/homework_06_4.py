# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in list:
    if number % 2 == 0:
        sum += number
print(sum)