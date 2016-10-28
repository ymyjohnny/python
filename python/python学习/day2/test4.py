#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''



def abc():
    start = 1
    end = 1001
    
    while 1:
        result = (start + end ) / 2
        i = raw_input("is number %d ?" % result)
        if i == 'bigger':
            end = result
        elif i == 'smaller':
            start = result
        elif i == 'eq':
            print 'You win,the number is %d' % result
            return

if __name__ == '__main__':    
    abc()
            
        
    