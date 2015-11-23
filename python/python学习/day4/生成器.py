#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


def func():
    result = []
    a = 1
    while a < 100000:
        result.append(a)
        a += 1
    return result 

for i in func():
    print i 