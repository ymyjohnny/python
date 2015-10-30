#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

class Wife():
    left_hand = 'chicken'
    right_hand = 'duck'
    
##成员函数检测 abc是否等于他的反序cba

# class R:
#     a =  'abcdef'
#     b = 'fedcba'
#     
#     def check(self):
#         return ''.join(list(reversed(self.a))) == self.b
#     
#     
# print R().check()

################3

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
       
       
################
def add(*l):
    s = 0
    for i in l:
       s += i
    return s
     
class Cauchy:
    def __init__(self, *l):
        self.l = list(l)
    def append(self,n):
        self.l.append(n)
        return self
    def call(self, function):
        return function(*self.l)

c = Cauchy(1,2,3)
#c.l = [1,2,3]
d = c.append(4)
#c.l=d.l=[1,2,3,4]
e = d.append(5)
#e.l = d.l = c.l = [1,2,3,4,5]
print e.call(add)
        
print Cauchy().append(1).append(2).append(3).append(4).append(5).call(add)       
       


class A:
    
    def __call__(self, a, b, c):
        return a+b+c
a = A()
print a(1,2,3)



# class Iter:
#     def __init(self, l):
#         pass
#     def next(self):
#         return self.l.pop()
# 
# i = Iter([1,2,3,4,5])
# print i.next()


















