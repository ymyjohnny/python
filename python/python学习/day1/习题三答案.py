#!/usr/bin/python
    #coding=utf-8

    
    
##########正确答案
#f = open('/home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt')
#s = f.read().decode('utf-8')

import os

s = os.popen('cat /home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt').read().decode('utf-8')
#f = open('/home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt')
#s = f.read().decode('utf-8')

# def split_and_extend(sep, chunks):
#      result = []
#      for chunk in chunks:

for line in s.splitlines():
    print line
    for i in line.split("，"):
        if i.startswith("但是") == True:
           print i
           
           
result1 = []
for line in s.splitlines():
    result1.append(line)

result2 = []
for chunk in result1:
    for chunk1 in chunk.split(u'，'):
        result2.append(chunk1)

result3 = []
for chunk in result2:
    for chunk1 in chunk.split(u'。'):
        reslut3.append(chunk1)