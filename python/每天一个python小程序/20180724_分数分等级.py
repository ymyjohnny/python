#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年7月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


sorce = int(raw_input('输入分数:\n'))
if sorce > 90:
    grade = 'A'
if  60 < sorce < 89:
    grade = 'B'
else :
    grade = 'C' 

print grade