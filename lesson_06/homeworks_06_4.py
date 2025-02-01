# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list = [1,2,3,4,5,6,7,5,4,9,12,15]

sum_of_even_items = 0

for num in list:
    if num % 2 == 0:
        sum_of_even_items += num

print(sum_of_even_items)
