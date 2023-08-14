#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    dmax = len(tuple_a)
    new_tuple = ()
    if len(tuple_b) > len(tuple_a):
        dmax = len(tuple_b)
    for i in range(0, dmax):
        if len(tuple_a) > i and len(tuple_b) > i:
            new_tuple = new_tuple + ((tuple_a[i] + tuple_b[i]),)
        elif len(tuple_a) <= i:
            new_tuple = new_tuple + (tuple_b[i],)
        else:
            new_tuple = new_tuple + (tuple_a[i],)

    return new_tuple
