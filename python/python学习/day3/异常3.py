#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''
import os

def test(basepath):
    try:
        for i in os.listdir(basepath):
            print i 
    except Exception:
            print Exception
    
def main():
    test('/tmp1')

if __name__ == '__main__':
    main()     