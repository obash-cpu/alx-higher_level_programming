#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    int_value = 0
    prev_value = 0

    for char in reversed(roman_string):
        if roman_to_int[char] >= prev_value:
            int_value += roman_to_int[char]
        else:
            int_value -= roman_to_int[char]
            prev_value = roman_to_int[char]

    return int_value
