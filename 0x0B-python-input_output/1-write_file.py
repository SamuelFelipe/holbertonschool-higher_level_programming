#!/usr/bin/python3

'''write into a file'''


def write_file(filename="", text=""):
    '''write into a file, if it doesn't exist create it'''

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
