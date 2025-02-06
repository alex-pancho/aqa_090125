count = 0
while count <= 5:
    print("in", count)
    count +=1

some_str = "Qwerty"
for char in some_str:
    print(char)

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

person_0 = {"name": "John", "age": 30, "city": "New York", "student": True, "year": 2022}
for key, value in person_0.items():
    print(key, ":", value)

person_2 = {"name": "Ace", "age": 16, "city": "New York", "student": True, "year": 2022}
person_3 = {"name": "Bill", "age": 20, "city": "New York", "student": False, "year": 2022}

students = [person_0, person_2, person_3]
for person in students:
    print(person["name"])
    age_of_person = person.get("age", 14)
    is_student = person.get("student", False)
    year_of_lerning = person["year"]

    if age_of_person >= 18:
        print("You are an adult")
        
        if is_student: 
            print("And you are a student")
            False # "", {}, [], (), 0
            current_year = 2024

            if current_year - year_of_lerning > 1:
                print("You are not first year student")
    else:
        print("You are not an adult.")

for i in range(10):
    if i == 7:
        print("Break викликаний на i =", i)
        break
    elif i == 4:
        print("continue викликаний на i =", i)
        continue
    else:
        print(i)
# else:
#     print("Break не викликаний")
