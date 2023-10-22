#! /usr/bin/env python

from collections import deque
from logic_gates import *

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
    p_c = 0
    r.appendleft(c_s)
    
    for i in range(len(a) - 2, -1, -1):
        p_c = c_c
        c_s, c_c = full_adder(int(a[i]), int(b[i]), c_c)
        r.appendleft(c_s)
    if(p_c != c_c): return None

    return [*r]

def get_twos_comp(val, bits):
    if(isinstance(val, int) == False): val = int(''.join(map(str,val)),2)
    if (val & (1 << (bits - 1))) != 0: val = val - (1 << bits)

    return val

def convert_twos_comp(a:list[int]) -> list[int]: return inc16(not16(a))

def sub16(a:list[int], b:list[int]) -> list[int]:

    """
    We can implement a n-bit subtractor using full_adders, as shown by this equation:
    A - B = A + (-B), where (-B) is the 2's complement of B.
    """
    comp_b = convert_twos_comp(b); return add16(a, comp_b)

def inc16(a:list[int]) -> list[int]: b = [0] * len(a); b[-1] = 1; return add16(a, b)

def dec16(a:list[int]) -> list[int]: b = [0] * len(a); b[-1] = 1; return sub16(a, b)

def ALU(x:list[int], y:list[int], zx:int, nx:int, zy:int, ny:int, f:int, no:int) -> list[int]:

    """
    Control bits:
    -------------
    zx, x = 0
    nx, x = !x
    zy, y = 0
    ny, y = !y
    f, 1: out = x + y, 0: out = x & y
    no, out = !out
    """

    """
    TODO:
        - Pad x or y if len(x) != 16 | len(y) != 16
        - Fix false positive overflow when x & y, x | y
    """

    """
    zx, nx
    """
    zeros_x = [0] * 16
    zero_x = mux16(x, zeros_x, zx)
    not_x = not16(zero_x)
    in_x = mux16(zero_x, not_x, nx)

    """
    zy, ny
    """
    zeros_y = [0] * 16
    zero_y = mux16(y, zeros_y, zy)
    not_y = not16(zero_y)
    in_y = mux16(zero_y, not_y, ny)

    """
    f
    """
    add_xy = add16(in_x, in_y)
    if(not add_xy): print("Overflow on addition!\n"); return -1
    and_xy = and16(in_x, in_y)
    f_xy = mux16(and_xy, add_xy, f)

    not_fxy = not16(f_xy)
    out = mux16(f_xy, not_fxy, no)

    notzr = or8way(out[:8]) | or8way(out[8:])

    zr = not notzr
    ng = out[0]

    return [out, zr, ng]
