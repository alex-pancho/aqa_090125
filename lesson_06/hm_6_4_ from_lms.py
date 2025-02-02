# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = sum([num for num in numbers if num % 2 ==0])
print(f"Cуммa усіх ПАРНИХ чисел в цьому лісті {numbers}: ", sum_of_even)