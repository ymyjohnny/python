#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''


import hashlib,os
import stat
import getopt,sys
import logging


ALGO = 'md5'

def getfiles(base):
    #print os.listdir(base)
    #result = []
    for filename in os.listdir(base):
        filepath = os.path.join(base, filename)
        #print filepath
        st = os.stat(filepath)
        yield filepath,st

      
        
def filter_type(source):
    for filepath, st in source:
        if stat.S_ISDIR(st.st_mode):
            continue
        yield filepath
     
def get_hash(filepath):
    print filepath
    h = getattr(hashlib, ALGO)()
    fi = open(filepath, 'rb')
    #print fi.read()
    #with open(filepath, 'rb') as fi:
    h.update(fi.read())
    return h.hexdigest()
    
       
def main():
    optlist, args = getopt.getopt(sys.argv[1:], 't:l:h')
    optdict =   dict(optlist)
    if '-l' in optdict:
         logging.basicConfig(level=getattr(logging, optdict['-l']))
    
    if '-t' in optdict:
        global ALGO
        ALGO = optdict['-t']
        
    for base in args:
      source = getfiles(base)
      source = filter_type(source)
      for filepath in source:
        h = get_hash(filepath)
        logging.info('%s(%s) => %s', ALGO, filepath, h)

    
if __name__ == '__main__':
    main()