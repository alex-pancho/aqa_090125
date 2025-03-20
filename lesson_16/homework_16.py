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
class Employee:
    def __init__(self, name:str, salary):
        self.name = name.title()
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department:str):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language:str):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__ (self, name, salary, department, programming_language, team_size:int):
        if not isinstance(name, str):
            raise TypeError("name повинно бути строкою")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("salary повинно бути невід'ємним числом")
        if not isinstance(department, str):
            raise TypeError("department повинно бути строкою")
        if not isinstance(programming_language, str):
            raise TypeError("Яprogramming_language повинно бути строкою")
        if not isinstance(team_size, int) or team_size < 0:
            raise ValueError("team_size повинно бути невід'ємним цілим числом")
        
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі 
порахуйте та виведіть в консоль площу та периметр кожної.

### Складність

Висока"
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(3.14 * (self.__radius ** 2), 2)

    def perimeter(self):
        return round(2 * 3.14 * self.__radius, 2)
    
    
Figures = [
    Square(5),
    Rectangle(4, 6),
    Circle(3)
]
print("*" * 30)
for Figure in Figures:
    print(f"Figure: {Figure.__class__.__name__}")
    print(f"Area: {Figure.area()}")
    print(f"Perimeter: {Figure.perimeter()}")
    print("*" * 30)

 """
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