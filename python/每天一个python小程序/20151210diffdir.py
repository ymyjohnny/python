#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-9
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import filecmp
import sys

try:
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
except:
    print 'Please input  diffdir.py dir1 dir2'
    sys.exit()

dirobject = filecmp.dircmp(dir1,dir2)
#dirobject.report()   比较当前指定目录的内容
#dirobject.report_partial_closure() 比较当前指定目录及第一级子目录中的内容
#dirobject.report_full_closure() 递归比较所有指定目录的内容
dirobject.report_full_closure()