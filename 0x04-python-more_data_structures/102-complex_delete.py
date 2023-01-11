#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_remove = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in keys_to_remove:
        del a_dictionary[key]
