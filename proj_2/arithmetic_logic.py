#! /usr/bin/env python

from collections import deque
from logic_gates import *

def half_adder(a:int , b:int) -> tuple[int, int]: return (a ^ b, a & b)

def full_adder(a:int, b:int, c:int) -> tuple[int, int]:

   s0, c0 = half_adder(a, b)

   s1, c1 = half_adder(c, s0)

   return (s1, c1 | c0)

def add16(a:list[int], b:list[int]) -> list[int]:

    #TODO: Maybe there is an alternative to the disgusting int cast
    r = deque()
    c_s, c_c = half_adder(int(a[-1]), int(b[-1]))
    r.appendleft(c_s)
    
    for i in range(len(a) - 2, -1, -1):
        c_s, c_c = full_adder(int(a[i]), int(b[i]), c_c)
        r.appendleft(c_s)

    print('\n',a,'\n',b)    
    if(c_c): r.appendleft(c_c)

    return [*r]

    
