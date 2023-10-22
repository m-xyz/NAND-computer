#! /usr/bin/env python

import numpy as np
import copy
import itertools
import unittest
from arithmetic_logic import *

half_adder_debug = {'00':(0,0), '01':(1,0), '10':(1,0), '11':(0,1)}
full_adder_debug = {'000':(0,0), '001':(1,0), '010':(1,0), '011':(0,1), '100':(1,0), '101':(0,1), '110':(0,1), '111':(1,1)}
half_subtractor_debug = {'00':(0,0), '01':(1,1), '10':(1,0), '11':(0,0)}
full_subtractor_debug = {'000':(0,0), '001':(1,1), '010':(1,1), '011':(0,1), '100':(1,0), '101':(0,0), '110':(0,0), '111':(1,1)}
ALU_CTRL_BITS = [([1,0,1,0,1,0],'0'),([1,1,1,1,1,1],'1'),([1,1,1,0,1,0],'-1'),([0,0,1,1,0,0],'x'),([1,1,0,0,0,0],'y'),([0,0,1,1,0,1],'nx'),([1,1,0,0,0,1],'ny'),([0,0,1,1,1,1],'-x'),([1,1,0,0,1,1],'-y'),([0,1,1,1,1,1],'x+1'),([1,1,0,1,1,1],'y+1'),([0,0,1,1,1,0],'x-1'),([1,1,0,0,1,0],'y-1'),([0,0,0,0,1,0],'x+y'),([0,1,0,0,1,1],'x-y'),([0,0,0,1,1,1],'y-x'),([0,0,0,0,0,0],'x&y')]

class TestGates(unittest.TestCase):

    def test_half_adder(self):
        for i in map(''.join, itertools.product('01', repeat=2)): self.assertEqual(half_adder(int(i[0]), int(i[1])), half_adder_debug[i])

    def test_full_adder(self):
        for i in map(''.join, itertools.product('01', repeat=3)): self.assertEqual(full_adder(int(i[0]), int(i[1]), int(i[2])), full_adder_debug[i])

    def test_half_subtractor(self):
        for i in map(''.join, itertools.product('01', repeat=2)): self.assertEqual(half_subtractor(int(i[0]), int(i[1])), half_subtractor_debug[i])

    def test_full_subtractor(self):
        for i in map(''.join, itertools.product('01', repeat=3)): self.assertEqual(full_subtractor(int(i[0]), int(i[1]), int(i[2])), full_subtractor_debug[i])

    def test_and_gate(self):
        for i in range(8):
            b = bin(i)[2:].zfill(3)
            self.assertEqual(Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).and_gate(),int(b[0]) & int(b[1]) & int(b[2]))

    def test_nand_gate(self):
        for i in range(8):
            b = bin(i)[2:].zfill(3)
            self.assertEqual(Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).nand_gate(), (not int(b[0]) & int(b[1]) & int(b[2])))

    def test_or_gate(self):
        for i in range(8):
            b = bin(i)[2:].zfill(3)
            self.assertEqual(Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).or_gate(), int(b[0]) | int(b[1]) | int(b[2]))

    def test_xor_gate(self):
        for i in range(8):
            b = bin(i)[2:].zfill(3)
            self.assertEqual(Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).xor_gate(),int(b[0]) ^ int(b[1]) ^ int(b[2]))

    def test_alu(self):
        def op_helper(x,y,op):

            match op:
                case '0': return [0] * 16
                
                case '1': return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

                case '-1': return [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

                case 'x': return x

                case 'y': return y

                case 'nx': return not16(x)

                case 'ny': return not16(y)

                case '-x': return convert_twos_comp(x)
#                    if(x[0] == 1): return x
#                    else: return convert_twos_comp(x)

                case '-y': return convert_twos_comp(y)
#                    if(y[0] == 1): return y
#                    else: return convert_twos_comp(y)

                case 'x+1': return inc16(x)

                case 'y+1': return inc16(y)

                case 'x-1': return dec16(x)

                case 'y-1': return dec16(y)

                case 'x+y': return add16(x,y)

                case 'x-y': return sub16(x,y)

                case 'y-x': return sub16(y,x)

                case 'x&y': return and16(x,y)

        x = list(np.random.choice([0, 1], size=(16,))); y = list(np.random.choice([0, 1], size=(16,)))

        for cb in ALU_CTRL_BITS:
            r = ALU(x,y,cb[0][0],cb[0][1],cb[0][2],cb[0][3],cb[0][4],cb[0][5])
            if(r == -1):
                print('\n==[OVERFLOW]=======================================================')
                print('X:',x,'\nY:',y,'\n')
                print('OP_CODE:',(cb[0][0],cb[0][1],cb[0][2],cb[0][3],cb[0][4],cb[0][5]))
                print('r >>>',r,'')
                print('===================================================================\n')
                continue
            dx = copy.deepcopy(x); dy = copy.deepcopy(y)
            dr = op_helper(dx,dy,cb[1])
            try:
                self.assertEqual(r[0] ,op_helper(dx,dy,cb[1]))
            except AssertionError:
                print('\n===================================================================')
                print('X:',x,'\nY:',y,'\n')
                print('OP_CODE:',(cb[0][0],cb[0][1],cb[0][2],cb[0][3],cb[0][4],cb[0][5]))
                print('r >>>',r,'')
                print('dr >>>',dr)
                print('===================================================================\n')

if __name__ == '__main__': unittest.main()
