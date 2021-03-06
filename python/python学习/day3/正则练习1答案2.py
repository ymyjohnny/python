#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''
#找出chardet.html里的url

import re

def grep_a(filepath, regex):
    f = open(filepath)
    source = f.read()
    f.close()
    return list(regex.findall(source))

def split_label(label):
    attrs = {}
    for attrstr in label.strip()[3:-1].split():
        r = attrstr.split('=', 1)
        if len(r) < 2:
            continue
        #print r
        k, v = r
        #print k
        #print v
        v = v.strip('" ')
        attrs[k] = v 
        return attrs

def main():
    regex = re.compile('<a[^>]*>' , re.MULTILINE)
    for label in grep_a('chardet.html',regex):
        attrs = split_label(label)
        if 'href'  in attrs:
            print attrs['href']
           #print attrs
        
if __name__ == '__main__':
    main()

