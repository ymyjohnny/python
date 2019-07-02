#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年7月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


l1= [1,1,1,3,4,2,1,2,2,1,5,7,7,7,444,23]

def uniq_list(l):
    L = []
    for i in l:
        if i not in L:
            L.append(i)
    return L

print uniq_list(l1)