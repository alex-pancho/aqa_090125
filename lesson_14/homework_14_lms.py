"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student():
    def __init__(self, name, surname, age, avg_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_score = avg_score

    def changing_score(self, new_score):
        self.avg_score = new_score


student_1 = Student("Leonid", "Svyatnyi", 29, 87)
print(student_1)
print(f"Імя студента: {student_1.name}\n"
      f"Прізвище: {student_1.surname}\n"
      f"Вік: {student_1.age}\n"
      f"Середній бал: {student_1.avg_score}")

new_score = float(input("Ведіть новий середній бал:"))

student_1.changing_score(new_score)
print(f"Імя студента: {student_1.name}\n"
      f"Прізвище: {student_1.surname}\n"
      f"Вік: {student_1.age}\n"
      f"Середній бал: {student_1.avg_score}")

