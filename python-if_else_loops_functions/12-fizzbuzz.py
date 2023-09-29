#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz ", end="")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz ", end="")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz ", end="")
            continue
        print(str(fizzbuzz) + ' ', end="")
