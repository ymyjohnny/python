#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

class R:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def check(self):
       return ''.join(list(reversed(self.a))) == self.b
   
r = R('abcdef','fedcba')
print r.a
print r.b
print r.check()
       

