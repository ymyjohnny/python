#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年11月15日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except:
    print 'please enter 20171115_idfa_chonghe.py text1 text2'
    sys.exit()

def readline(filename):
    f = open(filename,'r')
    text = f.read().splitlines()
    f.close()
    return text

text1_line = readline(sys.argv[1])
text2_line = readline(sys.argv[2])

for i in text1_line:
    if i in text2_line:
        print i

