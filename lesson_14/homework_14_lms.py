"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""
class Student():
    def __init__(self, name:str, surname:str, age:int, mark:int):
        self.name = f"ім'я: {name}"
        self.surname = f"прізвище: {surname}"
        self.age = f"вік: {age}"
        self.mark = f"середній бал: {mark}"

    def change_mark(self, new_mark: int):
        if new_mark < 0:
            raise ValueError ("New mark must be positive")
        if new_mark > 100:
            raise ValueError ("New mark must less than 100")
        self.mark = f"середній бал: {new_mark}"

student_1 = Student("Anna", "Dovhan", 28, 80)
print(f"Student_1: {student_1.name}, {student_1.surname}, {student_1.age}, {student_1.mark}")
student_1.change_mark(85)
print(f"Student_1: {student_1.name}, {student_1.surname}, {student_1.age}, {student_1.mark}")