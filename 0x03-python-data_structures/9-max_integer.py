#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        m = my_list[0]
        for i in range(1, len(my_list)):
            if m < my_list[i]:
                m = my_list[i]
        return m
