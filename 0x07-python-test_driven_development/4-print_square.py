#!/usr/bin/python3
"""
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    if size is a float and is less than 0, raise a TypeError
"""


def print_square(size):
    """if size is a float and is less than 0, raise a TypeError"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    """if size is less than 0"""
    if size < 0:
        raise ValueError("size must be >= 0")
    """if size is a float and is less than 0"""
    if type (size) == float and size < 0:
        raise TypeError("size must be an integer")
    for row in range (size):
        print('#' * size)
