#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-2
@author: ymy
'''

import re


s = 'frff,world!123.444.555.333'

#w 表示1-3位数字
w  = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}') 

m = re.search(w,s)

m1 = re.match(w,s)


if m:
    print  'search match'
    print m.group()


