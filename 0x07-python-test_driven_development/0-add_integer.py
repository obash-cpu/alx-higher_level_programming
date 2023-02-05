#!/usr/bin/python3
""" 0-add_integer Module """

def add_integer(a, b=98):
    """
    Adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        addition of two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
