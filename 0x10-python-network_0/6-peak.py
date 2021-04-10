#!/usr/bin/python3

'''find a peak in an array'''

def find_peak(list_of_integers):

    if not list_of_integers:
        return None
    elif len(list_of_integers) < 2:
        return list_of_integers[0]

    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i - 1] < list_of_integers[i]:
            if list_of_integers[i + 1] < list_of_integers[i]:
                return list_of_integers[i]
