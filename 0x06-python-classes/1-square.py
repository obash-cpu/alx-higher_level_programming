#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    def get_self(self):
        return self.__size

    def __set_size(self, value):
        self.__size = value
