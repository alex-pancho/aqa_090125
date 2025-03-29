from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    @property 
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
       

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

 
class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side
       

if __name__ == '__main__':

    figures = [
        Rectangle(34, 12),
        Circle(11),
        Square(21)
    ]

    for figure in figures:
        print(f"{figure.__class__.__name__}: Area = {figure.area():.2f}, Perimeter = {figure.perimeter():.2f}")
