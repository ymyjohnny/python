#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

#写一个函数 算出一堆数字的平均数，并做异常检测

def add(*l):
    s = 0
    for i in l:
        s += i 
    return (s /  len(l))

print add(1,2,3,4,5,6,7)
 
    
#if __name__ == '__main__':
   # main(l)
    