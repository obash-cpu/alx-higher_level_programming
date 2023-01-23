#!/usr/bin/python3
def raise_exception():
    try:
        a = 4
        b = "name"
        print(a / b)
    except TypeError:
        print("this is a type error")
