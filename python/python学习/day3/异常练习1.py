#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''


#使用os.*去操作一个不存在的文件(输入可以是数字么？)

#import os
        
def test(aa):
    a = raw_input('xx')
    a = int(a)
    #raise ValueError()

def main():
    try:
        test(11)
    #except ValueError:
    except Exception as error:
        print error

if __name__ == '__main__':
    main()
    
    
    
    
    