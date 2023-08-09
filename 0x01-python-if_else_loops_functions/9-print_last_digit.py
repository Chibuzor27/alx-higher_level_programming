#!/usr/bin/python3
def print_last_digit(number):
    n = int(number)
    if n < 0:
        n = n * (-1)
    n = n % 10
    print('{:d}'.format(n), end="")
    return n
