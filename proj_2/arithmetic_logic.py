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
    curr_sum, curr_carry = half_adder(int(a[-1]), int(b[-1]))
    r.appendleft(curr_sum)
    
    for i in range(len(a) - 2, -1, -1):
        curr_sum, curr_carry = full_adder(int(a[i]), int(b[i]), curr_carry)
        r.appendleft(curr_sum)

    print('\n',a,'\n',b)    
    if(curr_carry): r.appendleft(curr_carry)

    return [*r]

    
