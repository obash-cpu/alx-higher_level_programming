#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except:
        sys.stderr.write("Exception: {}\n".format(e))
        return (False)
    return (True)