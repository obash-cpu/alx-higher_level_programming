#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
    def width(self):
        return self.__width
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
            else:
                raise TypeError("width must be an integer")
    def height(self):
        return self.__height
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
            else:
                raise TypeError("height must be an integer")
