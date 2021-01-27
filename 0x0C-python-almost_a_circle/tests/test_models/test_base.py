#!/usr/bin/python3
import unittest
from models.base import Base
'''Classes functioning prove with Unittest'''

class TestBase(unittest.TestCase):
    '''test cases to the Base class'''

    def id_test(self):
        '''id assigment test'''
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(1, b1.id)
        self.assertEqual(13, b2.id)
        self.assertEqual(2, b3.id)
