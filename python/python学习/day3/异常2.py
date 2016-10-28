#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''


def add(a,b):
    try:
        a = int(a)
    except Exception:
        print Exception
    b=int(b)
    return a+b


def main():
    print add(1,'tt')
    
if __name__=='__main__' :
    main()
    