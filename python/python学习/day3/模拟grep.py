#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''
##模拟grep

import os, re, sys
from os import path
from os.path import join, getsize


def allfile(root):
    for base,dirs,files  in os.walk(root):
        for filename in files:
            filenpathes.append(filename)
    
def grepfile(filepath,regex):
    f = open(filepath)   
    for line in f:
        m = regex.match(line)
        if not m:
             continue
        sys.stdout.write(filepath + ':' + line)
        f.close()        
    
            
def main():
    filepathes = allfile(sys.argv[1])
    regex = re.compile(sys.argv[2])
    for filepath in filepathes:
        grepfile(filepathes, regex)


if __name__ == '__main__':
    main()

        

