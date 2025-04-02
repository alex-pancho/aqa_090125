import unittest
from abc import ABC, abstractmethod
import math
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

Напишіть тест, який перевіряє наявність атрібутів з `Manager` та `Developer` у класі `TeamLead`
"""
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department,  *args, **kwargs):
        super().__init__(name, salary, *args, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language, *args, **kwargs):
        super().__init__(name, salary, *args, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary, department, programming_language)
        self.team_size = team_size

#leader =  TeamLead("Anna", "50000", "QA automation", "Python", "10")


class TestTeamLeadAttributes(unittest.TestCase):
    def test_TeamLead_has_attributes(self):
        leader =  TeamLead("Anna", "50000", "QA automation", "Python", "10")

        self.assertTrue(hasattr(leader, "name"))
        self.assertEqual(leader.name, "Anna")

        self.assertTrue(hasattr(leader, "salary"))
        self.assertEqual(leader.salary, "50000")

        self.assertTrue(hasattr(leader, "department"))
        self.assertEqual(leader.department, "QA automation")

        self.assertTrue(hasattr(leader, "programming_language"))
        self.assertEqual(leader.programming_language, "Python")

        self.assertTrue(hasattr(leader, "team_size"))
        self.assertEqual(leader.team_size, "10")

if __name__ == "__main__":
    unittest.main()

"""
"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі 
порахуйте та виведіть в консоль площу та периметр кожної.
"""
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side + self.side + self.side + self.side

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


shapes = [
    Square(15),
    Rectangle(5, 10),
    Circle(7),
]

for shape in shapes:
    print(f"Figure: {shape.__class__.__name__}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print()








"""
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