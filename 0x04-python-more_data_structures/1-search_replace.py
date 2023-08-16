#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = [
            replace if my_list[i] == search else my_list[i]
            for i in range(0, len(my_list))
            ]
    return new_matrix
