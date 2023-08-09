#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    if n > 0:
        for i in range(0, len(str) - 1):
            if i != n:
                s = s + str[i:i+1]
        print('{:s}'.format(s))
    else:
        print('{:s}'.format(str))
