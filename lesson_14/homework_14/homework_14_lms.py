class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__average_grade = average_grade

    def __str__(self):
        return (
            f"Student: {self.__first_name} {self.__last_name}, age: {self.__age}, "
            f"average grade: {self.__average_grade:.2f}"
        )

    @property
    def average_grade(self):
        return self.__average_grade

    def update_grade(self, new_grade):
        self.__average_grade = new_grade
