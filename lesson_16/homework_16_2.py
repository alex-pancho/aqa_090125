#Завдання 2

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.__radius
    
class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        s = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(s *(s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c))
    
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

if __name__ == "__main__": 

    figures = [
        Circle(10),
        Rectangle(5, 8),
        Triangle(3, 4, 5)
    ]

    for figure in figures:
        print(f"{figure.__class__.__name__}: Area = {figure.area():.2f}, Perimeter = {figure.perimeter():.2f}")