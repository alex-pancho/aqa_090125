
message = "Some kind of text"
message2 = "Якийсь такий текст"
print(message, id(message))
message += " yet another text"
print(message, id(message))
print(message[0])
print(message[3])
print(message[5])
print(message[-1])

print(message[3:7])
print(message[1:12:2])
print(len(message))

for char in message:
    print(char)

hello = "hello"
world = " world"
h_w = hello + world
print(h_w)

split_msg = message.split()
print(split_msg)

fruit = "apple,orange,banana,grape"
split_msg2 = fruit.split(",",2)
print(split_msg2)

test_filename = "test_a"
print(test_filename.startswith("test"))
text_filename = "_readme.txt"
print(text_filename.endswith(".txt"))

upper_string = "ASD3REE"
print(upper_string.isupper())
lower_string = "hello"
print(lower_string.islower())
title_string = "Hello"
print(title_string.istitle())

username = "deRek hEller"
process_username = username.lower().title()
print(process_username)

start = message.find("n")
print(start)
next_n = message.find("n", start+1)
print(message[next_n:])

count_n = message.count("n")
print(count_n)

space_string = "    Привіт,      світ!    "
clean_str = space_string.strip()
print(clean_str)

space_string = "    Привіт,      світ!    zzzzzzzzzzzzzzz"
clean_str = space_string.strip().strip("z")
print(clean_str+"||")

clean_str = clean_str.replace("  ", " ").replace("  ", " ")
print(clean_str+"||")

fruit_list = ("apple", "orange", "banana")
join_up = ', '.join(fruit_list)
print(join_up)

str_number_1 = "12345"
int_number_1 = int(str_number_1)
print(int_number_1, type(int_number_1))

str_number_1 = "123.45"
int_number_1 = int(float(str_number_1))
print(int_number_1, type(int_number_1))

list_number = "1 ,2, 3 ,4,55"
list_number= list_number.replace(" ", "")
list_num = list_number.split(',')
print(list_num)

print(bool(list_number))
print(bool("")) # '', "", '''''', """""",

string = "False"
bool_var = bool(string)
print(bool_var)

get_first_fruit_capital = fruit_list[1].capitalize()
format_out = f"{get_first_fruit_capital} is better than {upper_string.lower()}"
print(format_out)

a = 2
b = 3

print(f"a + b = {a + b}")
pi = 3.141592
print(f"{pi:.2f}")

#print(f"{pi=}") # 3.8>
