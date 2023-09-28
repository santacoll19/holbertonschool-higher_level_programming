#!/usr/bin/python3
for number in range(0, 10):
    for i in range(0, 10):
        if number == i:
            continue
        if number > i:
            continue
        if number == 8 and i == 9:
            print('{}{}'.format(number, i))
            break
        print('{}{}, '.format(number, i), end="")
