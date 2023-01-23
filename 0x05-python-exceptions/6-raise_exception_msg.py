#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        a = b
    except NameError:
        print(message)
