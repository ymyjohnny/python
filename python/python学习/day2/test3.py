#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''
1

import math

def test(a,b,c):
    x = b*b -4*a*c
    x0 = math.sqrt(x)
    x1 = b+ x
    x2 = x1 % 2
    x3 = x2 % a
    print x,x0,x1,x2,x3
    return float(x3)
print test(1,2,1)


def test1(a,b,c):
    x = math.sqrt(b*b - 4*a*c)
    return  (-b+x) / (2*a), (-b-x) / (2*a)
print test1(2,7,3)
