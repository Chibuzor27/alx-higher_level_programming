#!/usr/bin/python3
for i in range(0, 100):
    print('{:02d}'.format(i), end="")
    print('{}'.format(', ' if i != 99 else '\n'), end="")
