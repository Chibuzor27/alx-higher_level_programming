#!/usr/bin/python3
flip = False
for i in range(97+26-1, 97-1, -1):
    if flip == False:
        print("{0:c}".format(i), end="")
        flip = not flip
    else:
        print("{0:c}".format(i - 97 + 65), end="")
        flip = not flip
