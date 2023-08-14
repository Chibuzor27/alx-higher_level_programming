#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) > 0:
        text = ""
        for i in range(0, len(my_string)):
            if not (my_string[i] == 'c' or my_string[i] == 'C'):
                text = text + my_string[i]
        return text
    else:
        return my_string
