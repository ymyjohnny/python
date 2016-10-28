#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''
#写一个函数，把2个输入值求和输出

def  sumtest(a,b):
    return a+b

print sumtest(4,68)

#匿名函数
print (lambda a,b:a+b)(5,7)

##参数不固定用*
def add(*l):
    s = 0
    for i in l:
        s += i 
    return s 
print add(1,2,3,4,5,6,7)
