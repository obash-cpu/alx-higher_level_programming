#!/usr/bin/python3
"""
     function that returns the list of available attributes and methods
"""


def lookup(obj):
    """Returns attributes amd methods of an object
    Args:
        obj: The object
        Return: The attributes and the methods of an object
    """
    return dir(obj)
