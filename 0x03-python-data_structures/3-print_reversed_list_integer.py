#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for integer in my_list:
        newlist = reversed(my_list)
        print("{}".format(newlist))
