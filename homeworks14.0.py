class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade
    
    def update_average_grade(self, new_grade):
        self.average_grade = new_grade
        print(f"Середній бал оновлено до: {self.average_grade}")
    
    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")

# Створюємо об'єкт студента
student1 = Student("Kontantins", "Ivanovs", 40, 85.5)

# Виводимо інформацію про студента
print("Інформація про студента:")
student1.display_info()

# Змінюємо середній бал
student1.update_average_grade(90.2)

# Виводимо оновлену інформацію
print("\nОновлена інформація про студента:")
student1.display_info()