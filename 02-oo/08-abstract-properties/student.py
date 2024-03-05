from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):

    @property
    @abstractmethod
    def perimeter(self):
        ...
    
    @property
    @abstractmethod
    def area(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width


    def perimeter(self):
        return 2 * (self.length + self.width)


    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius


    def perimeter(self):
        return 2 * pi * self.radius


    def area(self):
        return pi * self.radius ** 2
