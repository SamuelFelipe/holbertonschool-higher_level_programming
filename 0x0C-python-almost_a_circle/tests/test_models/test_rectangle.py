#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
'''Classes functioning prove with Unittest'''

class TestRectangle(unittest.TestCase):
    '''test cases to the Base class'''

    def id_test(self):
        '''id assigment test'''
        b1 = Rectangle(1, 1, 0, 0)
        b2 = Rectangle(1, 2, 0, 0, 13)
        b3 = Rectangle(1, 3, 0, 0)
        self.assertEqual(1, b1.id)
        self.assertEqual(13, b2.id)
        self.assertEqual(2, b3.id)

'''
    def str_test(self):
        pref = '[Rectangle] ({}) {}/{} - {}/{}'
        w = 5
        h = 2
        x = 1
        y = 0
        b1 = Rectangle(w, h, x, y)
        self.assertEqual(pref.format(1, w, h, x, y), str(b1))
'''
