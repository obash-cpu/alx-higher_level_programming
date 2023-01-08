#!/usr/bin/python3
def no_c(my_string):
    index = my_string.index("c", "C")
    my_string = my_string[:index] + my_string[index+1:]
    return my_string
