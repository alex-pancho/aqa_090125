print(2 == 2)
print(1 > 2)
print(1 < 2)
print(1 == 2)

print("a" == "a" )
print("a" == "A" )
print("a" == "aa")
print("a" >= "A" )
print("a" >= "aa")
expeced_result = "hello"
actual_result = "Hello Petro"
print(expeced_result.capitalize() in actual_result)
print(len(actual_result) >= 5)

if expeced_result in actual_result:
    print("I will run to you")
print("end")

answer = 43 # int(input("enter number:"))

if answer >= 42:
    print("LOOOK!!")
if answer == 42:
    print("Yes!!")
elif answer >= 43:
    print("Try somthing smaller")
elif answer <= 41 and answer >=0:
    print("Try somthing bigger")
else:
    print("That is not the correct answer. Please try again!")

apples_01 = "red"
apples_02 = "green"
is_plump = False
is_kivi = True

list_of_need_color = ["red", "green"]

if ((apples_01 in ["red", "green"] and 
    apples_02 in ["red", "green"])
    and
    (is_plump or is_kivi)):
    print("you can cook")

# if False:
#     print("sdsds")
