class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        """Инициализация атрибутов студента"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        """Метод для обновления среднего балла студента"""
        self.average_grade = new_grade
        print(f"🎯 Средний балл студента {self.first_name} {self.last_name} обновлён до {self.average_grade}")

    def display_info(self):
        """Метод для вывода информации о студенте"""
        print(f"\n📌 Информация о студенте:")
        print(f"👤 Имя: {self.first_name}")
        print(f"👤 Фамилия: {self.last_name}")
        print(f"🎂 Возраст: {self.age}")
        print(f"📊 Средний балл: {self.average_grade}")


# 🔥 Создание объекта студента
student1 = Student("Денис", "Ковилин", 22, 4.5)

# Вывод информации о студенте
student1.display_info()

# Обновление среднего балла
new_grade = float(input("\nВведите новый средний балл: "))
student1.update_average_grade(new_grade)

# Повторный вывод информации
student1.display_info()
