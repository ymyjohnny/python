#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

class  A:
    a = 10
    def mmx(self, b):
        print self.name, b 

class D(A):
    name = 'd'

a = A()
a.b = 20
a.name = 'bob'
d = D()

print A, A.a
print a, a.b, a.name
print d

a.mmx(20)
d.mmx(20)