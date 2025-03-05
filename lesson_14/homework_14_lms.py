"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""
class Student:
    def __init__(self, *, first_name:str, last_name:str, avg_score:float):
        self.first_name = first_name
        self.last_name = last_name
        self.__avg_score = avg_score

    def __repr__(self):
        return f"Student '{self.first_name} {self.last_name}' has average score: {self.__avg_score}"

    @property
    def avg_score(self):
        return '{:.1f}'.format(self.__avg_score)

    @avg_score.setter
    def avg_score(self, value:float):
        if isinstance(value, float | int) and value >= 0:
            self.__avg_score = value

student1 = Student(first_name='Sergey', last_name='Babych', avg_score=99.5)
print(student1)
print(student1.avg_score)
student1.avg_score = 1
print(student1.avg_score)