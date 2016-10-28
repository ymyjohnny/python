#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-24
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import re
import sys

#执行方法：python 20151124filter.py 上海第一傻逼
#返回：**第一**

filter_word = open('filter_word.txt' )

def get_keywords(k):
    for i in k.splitlines():
        #print i
        yield i
        
def filter_file(s, regex):
    for word in regex:
        if re.search(word, s):
            s = s.replace(word, '**')
            #print s
    print s       
            
def main():
    s = sys.argv[1]
    #print s 
    k  = filter_word.read()
    #print k
    regex = get_keywords(k)
    filter_file(s, regex)
    
    filter_word.close()

if __name__ == '__main__':
    main()    