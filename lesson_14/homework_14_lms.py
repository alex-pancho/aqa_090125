"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student():
    def __init__(self, first_name:str, last_name:str, age:int, avg_score:float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_score = avg_score
    
    def update_average_score(self, value):
        self.avg_score = value

rose_student = Student("Rose", "Tyler", 19, 4.8)

print("First Name:", rose_student.first_name)
print("Last Name:", rose_student.last_name)
print("Age:", rose_student.age)
print("Average sccore before update:", rose_student.avg_score)

rose_student.update_average_score(4.3)

print("Average sccore after update:", rose_student.avg_score)