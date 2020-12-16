#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    ret = []
    for i in my_list:
        if i % 2:
            ret.append(False)
        else:
            ret.append(True)
    return ret
