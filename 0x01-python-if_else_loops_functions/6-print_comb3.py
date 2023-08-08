#!/usr/bin/python3
for i in range(0, 100):
    rev = ((i % 10) * 10) + ((i - (i % 10)) / 10)
    if i < rev:
        print('{:02d}'.format(i), end="")
        print('{}'.format(', ' if i != 89 else '\n'), end="")
