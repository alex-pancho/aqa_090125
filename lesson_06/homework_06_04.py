#Є ліст з числами, порахуйте суму усіх ПАРНИХ чисел в цьому лісті
List_with_numbers = [9,12,33,44,15,2,9,0,59,77,25,99,123]
summa = 0
for number in List_with_numbers:
    if number % 2 == 0:
        summa += number
print(summa)