#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''
import re

def grep_a(filepath,regex):
    f = open(filepath)
    for line in f:
        line = line.strip()
        for m in regex.findall(line):
            
    f.close



if __name__ == '__main__':
    main():