#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

a = [1,2,3]
def test(*l):
    s = 0
    for i in a:
        s += i
    return s
print test()    

def test1(a,b,c):
    return c,b,a

c = test1(4,b=90,c=100)
print c
    
#reduce 迭代函数
def add1(x,y):
    return x+y
print  reduce(add1, range(1,3))




