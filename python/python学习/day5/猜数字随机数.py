#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''


import random

def main():
    start = 1
    end = 1000
    c = 0
    number = random.randint(start, end+1)
    #print number

    while True:
      in_number = raw_input("input (%d - %d) "  %(start, end))
      print number

      if in_number == 'quit':
         print '你猜了%d次' % c
         return
      in_number = int(in_number)
      if in_number == number:
        print "You win"
        c = c+1
        print '你猜了%d次' % c
        return
      if in_number > number:
        c = c+1
        print 'too big'
        end = in_number
      if in_number < number:
        c = c+1
        print 'too small'
        start = in_number + 1
    
    
if __name__ == '__main__':
    main()