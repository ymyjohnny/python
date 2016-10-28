#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''
#替换

class D(object):
    
    def __init__(self, trans_table):
        self.trans_table = trans_table
        self.a = 'hello, world'
        
    def geta(self):
        return self.__a
    
    def seta(self, a):
        for o, t in self.trans_table:
            a = a.replace(o, t)
#        a = a.replace('hello', '你好')
        self.__a = a
    
    a = property(geta, seta)
    
d = D([('hello','nihao'), ('world','shabi')])
print d.a
print type(d.a)
d.a = 'hello ymy'
print d.a
