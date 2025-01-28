# Tuple
empty_tuple = ()

single_element_tuple = (42,)
print(single_element_tuple, type(single_element_tuple))
single_element_tuple = (single_element_tuple[0], 52,)
print(single_element_tuple)

mixed_tuple = (1, 'hello', 3.14, True)
print(mixed_tuple)
print(mixed_tuple[0])
print(mixed_tuple[-1])

my_tuple = (1, 2, 3, 2, 4, 2, 5, "hi", "hello", "smth", 6, 7, 8, 9, 10)
what_we_look = 2
count_of_2 = my_tuple.count(what_we_look)
print(f"Count {what_we_look} in my_tuple:", count_of_2)
index_3 = my_tuple.index(3)
print("Index 2 in my_tuple:", index_3)

subset = my_tuple[2:9:2]
print(subset)

reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

user_a, user_b, c, d, *other = my_tuple
print(user_a)
print(user_b)
print(c)
print(d)
print(other)

my_list = [1, 2, 3, 'Python', True]
tuple_from_list = tuple(my_list)

# Виведення кортежу
print(tuple_from_list)

# List
my_list = ['MON', 'TUE', 'WED', 'THU', 'FRI']

print(my_list[0])
print(my_list[-1], id(my_list))

my_list.append("SAT")

print(my_list[-1], id(my_list))

my_inter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Отримати підмножину елементів з індексами вiд 2 до  7            
# (не включаючи 7) з кроком 2
subset = my_inter[2:7:2]
print(subset)

# my_list.append(["SUN", "ANY"])
my_list.extend(("SUN", "Any"))

print(my_list)
my_list.insert(-1, "la-la-la")
print(my_list)
my_list.remove("la-la-la")
print("my_list", my_list)
var = my_list.pop(-2)
print(var)
print(my_list)

print(my_list.index('WED'))
my_string = "kdfjsdlkfjdaklfjdfkldsjfkldasfjadl"
print(my_string.find("Tom"))
# print(my_list.index('dsdssWED'))
# ValueError: 'dsdssWED' is not in list
print('WED' in my_list)
print('Tom' in my_string)
print('fjsd' in my_string)


print("my_list", my_list)
first, *middle, last,  =  my_list[:3] # брати перші три
print(first)
print(middle)
print(last)

# sort та sorted 
new_sorted_list = sorted(my_list) #, reverse=True
print(new_sorted_list)
print(my_list.sort())
print(my_list)
my_int_list = [3, 6, 3, 4, 2, 1, 0 ,5, 7, 10.11, ]
my_int_list.sort()
print(my_int_list)
fruits =  ["яблуко", "апельсин", "банан", "bb", "бб", "груша", "слива",]
fruits_sorted = sorted(fruits, key=lambda x: len(x))
print(fruits_sorted)

my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)

my_range = range(1, 6)
list_from_range = list(my_range)
print(list_from_range)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# List comprehension 
squares = [x**2 for x in range(1, 10)]
print(squares)

# Set
fruits = {"яблуко", "банан", "апельсин"}
my_set = {1, 2, 4, 5, 3, 3, 3, 3,}
print(my_set)
print(3 in my_set)
popped_element = my_set.pop()
print(f"Видалений елемент: {popped_element}, Залишок: {my_set}")
my_set.remove(3)
print(3 in my_set)
print(my_set)
print(my_int_list)
unic = list(set(my_int_list))
print(unic)
my_set.update({3, 7})
print(my_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 3, 2, 1}

logical_union = set1.union(set2)
# logical_union = set1 | set2
print(logical_union)

logical_intersection = set1.intersection(set2)
# logical_intersection = set1 & set2
print(logical_intersection)

logical_difference = set1 - set2
print(logical_difference)
logical_difference_2 = set2 - set1
print(logical_difference_2)

logical_symmetric_difference = set1 ^ set2
print(logical_symmetric_difference)

print(set(my_string))

# Dictionary

en_ukr_dict = {"key":"ключ", "hi": "привіт", "love": "любов", "job": "робота",}
print(en_ukr_dict["key"])
print(en_ukr_dict["love"])
user = {'name': 'Василь', 'age': 25, 'city': 'Київ', (1, 2): "la-la-la", 1: 2163236}
print(user['age'])
print(user[(1, 2)])
print(user[1])
print('name' in user)
all_keys = user.keys()
all_vals = user.values()
print(all_keys, all_vals)
print("*" * 88)
for key  in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)

print(user.get('hhhage', 18))
