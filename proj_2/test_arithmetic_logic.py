#! /usr/bin/env python

from arithmetic_logic import *
import itertools

half_adder_debug = {'00':(0,0), '01':(1,0), '10':(1,0), '11':(0,1)}
full_adder_debug = {'000':(0,0), '001':(1,0), '010':(1,0), '011':(0,1), '100':(1,0), '101':(0,1), '110':(0,1), '111':(1,1)}


print('\n--- HALF_ADDER_TEST ---')
for i in map(''.join, itertools.product('01', repeat=2)):
    s, c = half_adder(int(i[0]), int(i[1]))
    ds, dc = half_adder_debug[i]
    try:
        assert ds == s and dc == c
        print('\t',i,s,c,'(PASSED)')
    except AssertionError: print('\t',i,s,c,'>>FAILED<<')


print('\n--- FULL_ADDER_TEST ---')
for i in map(''.join, itertools.product('01', repeat=3)):
    s, c = full_adder(int(i[0]), int(i[1]), int(i[2]))
    ds, dc = full_adder_debug[i]
    try:
        assert ds == s and dc == c
        print('\t',i,s,c,'(PASSED)')
    except AssertionError: print('\t',i,s,c,'>>FAILED<<')


#Write better test for add16
for i in itertools.product('01', repeat=4):
    for j in itertools.product('01', repeat=4):
        print(add16(i,j))
"""
M = 1 << 4
errs = []
for i in itertools.product('01', repeat=4):
    b0 = ''
    b0 = '0b' + b0.join(i)
    for j in itertools.product('01', repeat=4):
        b1 = ''
        b1 = '0b' + b1.join(j)
        r = bin(int(b1,2) + int(b0,2))
        dr = add16(i,j)[1]
        print(r,dr)
        try: assert r == dr
        except AssertionError: errs.append((i,j,r,dr))

for i in errs: print(i)
#print(add16([0,0,1,0], [1,1,0,0]))
"""
