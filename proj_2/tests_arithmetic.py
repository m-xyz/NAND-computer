#! /usr/bin/env python

import itertools
import unittest
from arithmetic_logic import *

half_adder_debug = {'00':(0,0), '01':(1,0), '10':(1,0), '11':(0,1)}
full_adder_debug = {'000':(0,0), '001':(1,0), '010':(1,0), '011':(0,1), '100':(1,0), '101':(0,1), '110':(0,1), '111':(1,1)}
half_subtractor_debug = {'00':(0,0), '01':(1,1), '10':(1,0), '11':(0,0)}
full_subtractor_debug = {'000':(0,0), '001':(1,1), '010':(1,1), '011':(0,1), '100':(1,0), '101':(0,0), '110':(0,0), '111':(1,1)}

class TestArithmeticGates(unittest.TestCase):

    def test_half_adder(self):
        for i in map(''.join, itertools.product('01', repeat=2)):
            s0, c0 = half_adder(int(i[0]), int(i[1]))
            s1, c1 = half_adder_debug[i]
            self.assertEqual(s1, s0) and self.assertEqual(c0, c1)

    def test_full_adder(self):
        for i in map(''.join, itertools.product('01', repeat=3)):
            s0, c0 = full_adder(int(i[0]), int(i[1]), int(i[2]))
            s1, c1 = full_adder_debug[i]
            self.assertEqual(s0, s1) and self.assertEqual(c0, c1)

    def test_half_subtractor(self):
        for i in map(''.join, itertools.product('01', repeat=2)):
            d0, b0 = half_subtractor(int(i[0]), int(i[1]))
            d1, b1 = half_subtractor_debug[i]
            self.assertEqual(d0, d1) and self.assertEqual(b0, b1)

    def test_full_subtractor(self):
        for i in map(''.join, itertools.product('01', repeat=3)):
            d0, b0 = full_subtractor(int(i[0]), int(i[1]), int(i[2]))
            d1, b1 = full_subtractor_debug[i]
            self.assertEqual(d0, d1) and self.assertEqual(b0, b1)

if __name__ == '__main__': unittest.main()
