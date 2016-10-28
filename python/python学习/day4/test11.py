#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


def fib(n):
    if n < 1: return 1
    return fib(n-1) + fib(n -2)
