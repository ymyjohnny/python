#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''
import json
import os
from os import path

SAVEFILE = 'day45.save'

def main():
    start = 1
    end = 1001
    if path.exists(SAVEFILE):
        f = open(SAVEFILE)
        start, end = json.load(f)
        f.close()
    while True:
        current = (start + end) / 2
        i = raw_input('is number %d?' % current)
        if i == 'quit':
            return
        elif i == 'big':
            end = current
        elif i == 'small':
            start = current + 1
        elif i == 'eq':
            print current
            os.remove(SAVEFILE)
            return
        f = open(SAVEFILE, 'w')
        json.dump((start, end), f)
        f.close()

if __name__ == '__main__': main()
    
    
    
    
    
    
    
    
    