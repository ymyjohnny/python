#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-23
@author: ymy
'''


import re
import subprocess

def get_process(s):
    Process = subprocess.check_output(["ps","-ef"]).splitlines()
    #print Process
    for line in Process:
        if  re.search(s, line):
            yield line
              
def get_pid(lines):
    for line in lines:
        pid = line.split()[1]
        print pid
    
      
def main():
    s = 'java'
    source = get_process(s)
    get_pid(source)
    
        
if __name__ == '__main__':
    main()