#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''
import random
import string

#字母字符串
string.letters

#字母+数字+特殊符号字符串
s = string.printable

#print random.choice(string.letters)

mima = ''.join([random.choice(s) for i in xrange(20)])

print mima

