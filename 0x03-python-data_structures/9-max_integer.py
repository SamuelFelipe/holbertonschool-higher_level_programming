#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        l_min = my_list[0]
        for i in my_list:
            if i > l_min:
                l_min = i
        return l_min
    return None
