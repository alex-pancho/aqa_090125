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

Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі 
порахуйте та виведіть в консоль площу та периметр кожної.

"""

# Завдання 1
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



# Завдання 2
from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, a):
        self.__a = a

    def area(self):
        return self.__a ** 2

    def perimeter(self):
        return self.__a * 4
    

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c 
    

class Circle(Figure):
    def __init__(self, r):
        self.__r = r

    def area(self):
        return math.pi * self.__r ** 2

    def perimeter(self):
        return 2 * math.pi * self.__r
    



if __name__ == "__main__":
    team_lead = TeamLead("John", 5000, "IT", "Python", 5)
    print(team_lead.department)
    print(team_lead.programming_language)
    print(team_lead.team_size)

    square = Square(5)
    triangle = Triangle(3, 4, 5)
    circle = Circle(10)

    figures = [square, triangle, circle]

    for figure in figures:
        print(f"Area: {figure.area()}, Perimeter: {figure.perimeter()}")
