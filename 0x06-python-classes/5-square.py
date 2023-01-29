#!/usr/bin/python3
"""
    Square generation module for Python project 0x06
"""
class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square

    Attributes:
        __size (int): length of one side of square

    """

    def __init__(self, size=0):
        # attribute assigment here engages setters defined below
        self.size = size

        @property
     def size(self):
         """__size getter, setter with same method name
            Returns:
                area (int): length of one side, squared
         """
         area = self.__size * self.__size

         return area
     def my_print(self):
         """Prints text representation of square in hash chars.

         Attributes:
            __size (int): length of one side of square
        """
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
                print()
        if self.__size is 0:
            print()
