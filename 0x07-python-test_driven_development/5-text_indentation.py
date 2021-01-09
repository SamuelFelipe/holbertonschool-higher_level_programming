#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    n = True
    for i in text:
        if n or i != ' ':
            print(i, end='')
        n = True
        if i in ['.', '?', ':']:
            n = False
            print('\n')
