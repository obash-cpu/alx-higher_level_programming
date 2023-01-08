#!/usr/bin/python3
def no_c(my_string):
    my_string1 = list(my_string)
    index = my_string1.index("c" or "C")
    my_string1 = my_string1[:index] + my_string1[index+1:]
    return my_string1
