#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) == str) is False or roman_string is None:
        return 0
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    output = 0
    for letters in range(len(roman_string)):
        now = rom_num[roman_string[letters]]
        if letters != 0:
            prev = rom_num[roman_string[letters - 1]]
            if now > prev:
                output = output - prev - prev
        output += now
    return (output)
