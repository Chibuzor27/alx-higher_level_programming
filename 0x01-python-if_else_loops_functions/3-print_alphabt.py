#!/usr/bin/python3
for i in range(97, 97+26):
    if chr(i) not in 'qe':
        print("{0:c}".format(i), end="")
