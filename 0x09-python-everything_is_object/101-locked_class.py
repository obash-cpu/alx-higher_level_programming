#!/usr/bin/python3
"""
A class that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.

Attributes:
    first_name (str): first name of something.
"""
class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"
