#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
beg_string = f"Last digit of {number}"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"{beg_string} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{beg_string} is {last_digit} and is 0")
else:
    print(f"{beg_string} is {last_digit} and is less than 6 and not 0")
