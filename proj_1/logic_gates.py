#!/usr/bin/env python

import typing
import math

"""
Logic gates to build:
    - NAND [X]
    - NOT [X]
    - AND [X]
    - OR [X]
    - XOR [X]
    - MUX [X]
    - DMUX [X]
    - NOT16
    - OR16 [X]
    - MUX16 [X]
    - OR8WAY
    - MUX4WAY16
    - MUX8WAY16
    - DMUX4WAY16
    - DMUX8WAY16

"""

class Gate(object):

    def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.L = list(self.__dict__.values())

    def nand_gate(self) -> int: return self.not_gate(self.and_gate())

    def not_gate(self, r:int) -> int: return not r

    def not_n_gate(self, a:list[int]) -> None: return [int(self.not_gate(i)) for i in a]

    def and_gate(self) -> int:

        b = self.L[0]

        for i in range(1, len(self.L)): b = b & self.L[i]

        return b

    def or_gate(self) -> int:
        
        b = self.L[0]

        for i in range(1, len(self.L)): b = b | self.L[i]

        return b

    def xor_gate(self) -> int:

        b = self.L[0]

        for i in range(1, len(self.L)): b = b ^ self.L[i]

        return b

    #math.ceil(math.log2(len(self.__dict__) - 1))
    def mux_gate(self, sel): 
        try: return self.L[int(str(sel), 2)]
        except IndexError: print("Invalid selector!\n")

    def demux_gate(self, sel, _in):
        try: self.L[int(str(sel), 2)] = _in
        except IndexError: print("Invalid selector!\n")

    def __repr__(self): return f'<undefined> gate with inputs: {self.__dict__}'

def test_gates():
    print('\n--- Testing AND ---')
    for i in range(8):
        b = bin(i)[2:].zfill(3)
        try:
            assert Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).and_gate() == int(b[0]) & int(b[1]) & int(b[2])
            print(b,' : (PASSED)')
        except AssertionError as m:
            print(b,' : >>FAILED<<')

    print('\n--- Testing NAND ---')
    for i in range(8):
        b = bin(i)[2:].zfill(3)
        try:
            assert Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).nand_gate() == (not int(b[0]) & int(b[1]) & int(b[2]))
            print(b,' : (PASSED)')
        except AssertionError as m:
            print(b,' : >>FAILED<<')

    print('\n--- Testing OR ---')
    for i in range(8):
        b = bin(i)[2:].zfill(3)
        try:
            assert Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).or_gate() == int(b[0]) | int(b[1]) | int(b[2])
            print(b,' : (PASSED)')
        except AssertionError as m:
            print(b,' : >>FAILED<<')

    print('\n--- Testing XOR ---')
    for i in range(8):
        b = bin(i)[2:].zfill(3)
        try:
            assert Gate(a=int(b[0]), b=int(b[1]), c=int(b[2])).xor_gate() == int(b[0]) ^ int(b[1]) ^ int(b[2])
            print(b,' : (PASSED)')
        except AssertionError as m:
            print(b,' : >>FAILED<<')

