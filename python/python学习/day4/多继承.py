#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''

class  B(object):
    x = 1

class C(object):
    x = 2

class D(B, C):
    pass

d = D()
print d.x

##x被多次定义的时候  继承前一个函数的值