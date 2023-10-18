#! /usr/bin/env python

from collections import deque
from logic_gates import *
import copy

def half_adder(a:int , b:int) -> tuple[int, int]: return (Gate(a=a,b=b).xor_gate(), Gate(a=a,b=b).and_gate())

def half_subtractor(a:int , b:int) -> tuple[int, int]: return (Gate(a=a,b=b).xor_gate(), Gate(a=not a,b=b).and_gate())

def full_adder(a:int, b:int, c:int) -> tuple[int, int]:

   s0, c0 = half_adder(a, b)

   s1, c1 = half_adder(s0, c)

   return (s1, c0 | c1)

def full_subtractor(a:int, b:int, c:int) -> tuple[int, int]:

    d0, b0 = half_subtractor(a, b)

    d1, b1 = half_subtractor(d0, c)

    return (d1, b0 | b1)

def add16(a:list[int], b:list[int]) -> list[int]:

    #TODO: Maybe there is an alternative to the disgusting int cast
    c_s, c_c = half_adder(int(a[-1]), int(b[-1])); r = deque()
    r.appendleft(c_s)
    
    for i in range(len(a) - 2, -1, -1):
        c_s, c_c = full_adder(int(a[i]), int(b[i]), c_c)
        r.appendleft(c_s)

    if(c_c): r.appendleft(c_c)

    return [*r]

def sub16(a:list[int], b:list[int]) -> list[int]:

    c_d, c_b = half_subtractor(int(a[-1]), int(b[-1])); r = deque()
    r.appendleft(c_d)
    
    for i in range(len(a) - 2, -1, -1):
        c_d, c_b = full_subtractor(int(a[i]), int(b[i]), c_b)
        r.appendleft(c_d)

    if(c_b): r.appendleft(c_b)

    return [*r]


def inc16(a:list[int]) -> list[int]: b = [0] * len(a); b[-1] = 1; return add16(a, b)

def dec16(a:list[int]) -> list[int]: b = [0] * len(a); b[-1] = 1; return sub16(a, b)
