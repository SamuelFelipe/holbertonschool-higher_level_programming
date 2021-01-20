#!/usr/bin/python3

"""Class that inherits from list"""


class MyList(list):
    '''Subclass of list'''

    def print_sorted(self):
        '''Print the list sorted'''
        print(sorted(self))
