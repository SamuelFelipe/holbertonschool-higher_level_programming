#!/usr/bin/python3

'''Class MyList'''


class MyList(list):
    '''Subclass of list'''

    def print_sorted(self):
        '''Print the list sorted'''
        print(sorted(self))
