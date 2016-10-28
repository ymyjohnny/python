#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

l = [1,2,3,4,5]

# def  add(a,b,c=5):
#     return a+b+c 
# print add(l[3],1)

def add(l,i=0):
    return sum(l) + i


print add([1,2,3,4,5],1)
print add([],1)

#lambda 函数 连乘
print reduce(lambda x,y:x*y,[1,2,3,4,6])

def reduce(fuction,l):
    while len(l) > 1:
        a = l.pop(0)
        b = l.pop(0)
        c = fution(a,b)
        l.insert(0,c)
    return l[0]

def reduce1(fuction,l,inital):
    r = inital
    for i in l:
        r = fuction(r,i)
    return r




