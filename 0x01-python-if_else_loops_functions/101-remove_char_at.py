#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    if n > 0:
        for i in range(0, len(str)):
            if i != n:
                s = s + str[i:i+1]
        return s
    else:
        return str
