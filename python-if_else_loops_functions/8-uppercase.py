#!/usr/bin/python3
def uppercase(str):
    new_string = ""

    for i in str:
        a = ord(i)
        if a >= 97 and a <= 122:
            b = a - 32
            new_string += chr(b)
        else:
            new_string += i
    print("{:s}".format(new_string))
