#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{}".format(result))
    except:
        result = None
    finally:
        print("{}".format(result))
        return result
