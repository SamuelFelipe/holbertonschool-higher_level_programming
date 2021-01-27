#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test(self):
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(1, b1.id)
        self.assertEqual(13, b2.id)
        self.assertEqual(2, b3.id)
