#!/usr/bin/python3
"""
Square generation module for Python project 0x06
"""

class Square:
    def __init__(self, size=0):
        self.__size = size

square1 = Square()
try:
    int(square1.size) = True
except TypeError:
    print("size must be an integer")
elif:
    try:
        size < 0
    except ValueError:
        print("size must be >= 0")
