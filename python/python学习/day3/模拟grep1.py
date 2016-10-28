#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-2
@author: ymy
'''

import os,re,sys
from __builtin__ import str

dirname = '/tmp'

def allfile(dirname):
    filenames = []
    for base,dirs,files in os.walk(dirname):
        for file in files:
            filename = os.path.join(base,file)
            #print filename
            filenames.append(filename)
    #print filenames
            #print filenames

def grep_a(file,regex):
    f = open(file)
    for line in f:
        m = regex.match(line)
        if m:
            print file + ':' + line
    f.close()
    
#  r = re.compile('test')
# grep_a('/home/ymy/workspace/python/python学习/day3/test.py' ,r )

def main():
    files = allfile(sys.argv[2])
    print files
    regex = re.compile(sys.argv[1])
    print regex
    for filepath in files:
        grep_a(filepath,regex)
 
if __name__ == '__main__':
    main()
   
