#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''

#找出chardet.html里的url

import os, re, sys

def grepfile(text):
    txt = os.popen('cat chardet.html').read().splitlines()  
    for i in txt:
        m = re.match(txt)
        if not m:
             continue
        sys.stdout.write(txt)
    txt.close()
    
    
def main():
    text = '*href*
    grepfile(text):       
    
if __name__ == '__main__':
    main()