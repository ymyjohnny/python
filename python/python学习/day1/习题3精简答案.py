#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''
#from chardet.test import result
import os
s = os.popen('cat /home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt').read().decode('utf-8')
#f = open('/home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt')
#s = f.read().decode('utf-8')

def split_and_extend(sep, chunks):
     result = []
     for chunk in chunks:
         result.extend(chunk.split(sep))
         return result

def splits(s,seps):
    result = [s,]
    for i in seps:
        result = split_and_extend(i, result)
        return result

#result = [s,]
#result = 

result = splits(s, u'\n  ，。“‘')
result = [chunk.strip() for chunk in result]
result = [chunk for chunk in result if chunk.startswith(u'但是')]

num = len(result)
print num


