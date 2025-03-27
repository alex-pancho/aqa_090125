"""
Завдання 1

Створіть клас **`Employee`**, який має атрибути **`name`** та **`salary`**.
Далі створіть два класи, **`Manager`** та **`Developer`**, які успадковуються від **`Employee`**.
Клас **`Manager`** повинен мати додатковий атрибут **`department`**, а клас **`Developer`** -
атрибут **`programming_language`**.

Тепер створіть клас **`TeamLead`**, який успадковується як від **`Manager`**, так і від **`Developer`**.
Цей клас представляє керівника з команди розробників. Клас **`TeamLead`** повинен мати всі атрибути як
**`Manager`** (ім'я, зарплата, відділ), а також атрибут **`team_size`**, який вказує на кількість розробників
у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрібутів з `Manager` та `Developer` у класі `TeamLead`"""

import unittest
import math
from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

team_lead = TeamLead("Vasyl", 1000, "DPRK", "Python", 5)
print(f'Team lead name: {team_lead.name}, Team lead salary: {team_lead.salary}, Team lead department: {team_lead.department}, Program.language: {team_lead.programming_language}, Team size: {team_lead.team_size}')


class TestTeamLead(unittest.TestCase):
    def test_teamlead_manager_dev_attr(self):
        """Check for presence of attributes from calss Manager and Developer in class TeamLead"""
        team_lead = TeamLead("Alice", 5000, "SuperDep", "Python, C#", 125)
        
        self.assertTrue(hasattr(team_lead, "department"), "TeamLead має атрибут 'department'")
        self.assertTrue(hasattr(team_lead, "programming_language"), "TeamLead має атрибут 'programming_language'")
        self.assertTrue(hasattr(team_lead, "team_size"), "TeamLead має атрибут 'team_size'")

if __name__ == "__main__":
    unittest.main(verbosity=2)


"""Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі 
порахуйте та виведіть в консоль площу та периметр кожної.

### Складність

Висока

# Як робити домашне завдання у Git

1. **ОБОВ’ЯЗКОВО с**творіть нову гілку, яка буде використовуватись для змін, за 
    допомогою команди `git checkout -b homework##`
2. **Виконайте ДЗ у окремому файлі homework_<#lesson>.py**
3. Зробіть коміт з змінами, додавши опис виконаних змін
4. Відправте свої зміни до вашого репозиторію 
5. Створіть pull request у  власну гілку `main` на головний репозиторію 
    [https://github.com](https://github.com/), натиснувши кнопку "New pull request" на
    відповідному розділі репозиторію.
6. Назначте ревьювером викладача
7. **Посилання на PR вставте у форму відповіді для ДЗ в навчальній системі**
"""

class Figure(ABC):
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        square_rectangle = self.width * self.height
        return f'Square of rectangle = {square_rectangle}'
        
    def perimeter(self):
        perim_rectangle = 2 * (self.width + self.height)
        return f'Perimeter of rectangle = {perim_rectangle}'

class ІsoscelesTriangle(Figure): # рівнобедрений трикутник
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def square(self):
        height = math.sqrt(self.side_a**2 - (self.side_b/2)**2)
        square_iso_triangle = 1/2 * height * self.side_b
        return f'Square of isoceles triangle = {square_iso_triangle}'
    
    def perimeter(self):
        perim_iso_triangle = 2 * self.side_a + self.side_b
        return f'Perimeter of isoceles triangle = {perim_iso_triangle}'
    
class Square(Figure):
    def __init__(self, side_of_square):
        self.side_of_square = side_of_square

    def square(self):
        s_of_square = self.side_of_square * self.side_of_square
        return f'Square of figure square = {s_of_square}'
    
    def perimeter(self):
        perim_of_square = 4 * self.side_of_square
        return f'Perimeter of figure square = {perim_of_square}'

square_figure = Square(4)
print(square_figure.square())
print(square_figure.perimeter())

trian = ІsoscelesTriangle(10, 16)
print(trian.square())
print(trian.perimeter())
        
rectangle = Rectangle(4,5)
print(rectangle.square())
print(rectangle.perimeter())