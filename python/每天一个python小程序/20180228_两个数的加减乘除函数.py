#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年2月28日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

def  x_y(x,y):
    jia = x + y
    print "x+y=%s "   % jia
    jian = x - y
    print "x-y=%s "   % jian
    cheng = x * y
    print "x*y=%s "   % cheng
    #除法需要先把被除数的类型int转为float
    chu = x /  float(y)
    print "x/y=%s "   % chu
    
def main():
    x_y(50,6)
    a.splitlines()


if __name__ == '__main__':
    main()