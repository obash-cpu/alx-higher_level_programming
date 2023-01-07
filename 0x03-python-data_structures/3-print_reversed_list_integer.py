#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newlist = list(range(len(my_list)[::-1]))
    print("{}".format(newlist))
