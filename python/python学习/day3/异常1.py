#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

class A(Exception):
    pass

def add(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        ##准备捕获
        raise A()
    return a+b 


def main():
    
###抓取异常
    try:
         print add(1,'2')
    except Exception as a:
        print type(a)
    
if __name__ == '__main__'  : main()
