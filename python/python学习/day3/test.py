#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-5
@author: ymy
'''


def  jiafa(a,b):
    return a+b

def main():
    try:
        print jiafa(1,'a')
    except Exception as error:
        print error
        
if __name__ == '__main__':
    main()