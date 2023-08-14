#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    dmax = len(tuple_a)
    if len(tuple_b) > len(tuple_a):
        dmax = len(tuple_b)
    new_tuple = tuple([
        (tuple_a[i] if i < len(tuple_a) else 0) +
        (tuple_b[i] if i < len(tuple_b) else 0)
        for i in range(0, dmax)])
    return new_tuple
