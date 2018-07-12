#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年12月22日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j) and (k != j):
                print  (i,j,k)