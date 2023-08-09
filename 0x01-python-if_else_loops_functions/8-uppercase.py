#!/usr/bin/python3
def uppercase(str):
    n = ""
    for i in range(0, len(str)):
        c = str[i:i+1]
        asc = ord(c)
        if (asc >= 97) and (asc < (97 + 26)):
            n = n + chr(asc-97+65)
        else:
            n = n + c
    print('{:s}'.format(n))
