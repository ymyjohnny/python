#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

a = raw_input()

def test(*l):
    s = 0
    for i in l:
        s = i 
    if a < s:
        s = int(s) / 2
    elif a > s:
        x = 'too larger'
    elif a == s:
        x = 'You Win'
    return s,x



print test(1,2,3,4,5,6,7,8,9,10)
      



