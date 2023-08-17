#!/usr/bin/python3
def uniq_add(my_list=[]):
    tracker = []
    ttl = 0
    for i in range(0, len(my_list)):
        if my_list[i] not in tracker:
            tracker.append(my_list[i])
            ttl = ttl + my_list[i]
    return ttl
