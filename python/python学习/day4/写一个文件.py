#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-14
@author: ymy
'''


fout = open("test.txt","w")

#fout = open("test.txt","a")   a为追加   w为覆盖写入

fout.write(" i love heisi\n")

fout.close

fin = open("读写json文件.py","r+")

str =  fin.read()
print str 
fin.close