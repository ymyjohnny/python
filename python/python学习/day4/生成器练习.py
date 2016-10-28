#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''

##如果要读入很多数据处理的话会占用较大内存，用生成器一个个读取数据会节约内存开销

def func():
    a = 1 
    while a < 10:
        yield a
        a += 1
    print   'here'
    a = 1 
    while a < 10:
        yield a
        a += 1


def main():
     for i in func():
         print i   
        
if __name__ == '__main__':
    main()