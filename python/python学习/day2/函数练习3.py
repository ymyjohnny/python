#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''
import math
    
# 算平方根
def test1(a,b,c):
    x = math.sqrt(b*b - 4*a*c)
    return  (-b+x) / (2*a), (-b-x) / (2*a)
print test1(2,7,3)