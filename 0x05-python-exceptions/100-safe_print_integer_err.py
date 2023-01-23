#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{}".format(int(value)))
        return (True)
    except:
        sys.stderr.write("Exception: {}\n".format(e))
        return (False)
