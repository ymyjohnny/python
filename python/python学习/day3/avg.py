#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

#写一个函数 算出一堆数字的平均数，并做异常检测
import sys

def numlist(a,b):
    list = range(a,b+1)
    return list

def main():
    testa = int(sys.argv[1])
    testb = int(sys.argv[2])
    data = numlist(testa,testb)
    print data
    sum = 0
    for i in data:
        sum += i
        print sum
        avg = sum/len(data)
    print avg

if __name__ == '__main__':
    main()
 
    
#if __name__ == '__main__':
   # main(l)
    