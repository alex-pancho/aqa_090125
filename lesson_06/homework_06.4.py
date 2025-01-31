# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
List_with_numbers = [1, 2, 45, 7, 56, 83, 29, 61, 34, 78, 15, 90, 64]
sum = 0
for number in List_with_numbers:
    if number % 2 == 0:
        sum += number
print(sum)
