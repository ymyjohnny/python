#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-10-28
@author:ymy
Copyright ymyjohnny@gmail.com
'''


for letter in 'Python':     # First Example
    if letter == 'h':
         break
    print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
    print 'Current variable value :', var
    var = var -1
    if var == 5:
        break