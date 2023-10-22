#!/usr/bin/env python

import typing
import math

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

def mux16(a:list[int], b:list[int], sel:int) -> list[int]:

    if(sel == 0): return a
    elif(sel == 1): return b
    return None

def not16(a:list[int]) -> list[int]: return [int(not i) for i in a]

def and16(a:list[int], b:list[int]) -> list[int]: return [a[i] & b[i] for i in range(len(a))]

def or8way(a:list[int]) -> int:

    b = a[0]

    for i in range(1, len(a)): b = b | a[i]

    return b


