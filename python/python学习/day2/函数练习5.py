#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-27
@author: ymy
'''
#猜数字，计算机有个数，人来猜

def Checknumber(a):
    people = input("input number")
    people = int(people)
    #raise ValueError()
    try :     
            int(people)
    except Exception:
            print Exception


def main():
    number = 666
    people = 0
   
    while  people != number :
            people = input("input number  ")
            if Checknumber(people) > number:
                print 'bigger'
            elif people < number:
                print 'smaller'
            elif people == number:
                print 'you win,the number is  %d'   % number
                return
        
    
if __name__ == '__main__': 
    main()