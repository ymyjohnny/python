#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

def split_and_extend(sep, chunks):
    result = []
    for chunk in chunks:
        result.extend(chunk.split(sep))
    return result

def splits(s,seps):
    result = [s,]
    for i in seps:
        result = split_and_extend(i,result)
    return result

f = open('少年pi的奇幻漂流 中文版.txt')
def procx(f):
    s = f.read().decode('utf-8')
    result = splits(s,u'\n，。”')
    result = [chunk.strip() for chunk in result]
    result = [chunk for chunk in result if chunk.startswith(u'但是')]
    return len(result)
print procx(f)

class FileObject:
    def __init__(self, s):
        self.s = s
        
    def read(self):
        return self.s 

    def readlines(self):
        return self.s.splitlines()

    
print procx(FileObject('但是，可是，也许，但是'))    
 
    
     






