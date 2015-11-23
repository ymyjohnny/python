#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''

# f = open('少年pi的奇幻漂流 中文版.txt')
# s = f.read().decode('utf-8')
# result = splits(s, u'\n，。"')
# 
# def  chunk1():
# #result = [chunk.strip() for chunk in result]
#    for chunk in result:
#       yield chunk
#       result = chunk.strip()
#       return result
#      
# #result = [chunk for chunk in result if chunk.startswith(u'但是')]
# def chunk2():
#   for chunk in result:
#     yield chunk
#     if chunk.startswith(u'但是'):
#         chunk

def strip_map(s):
    result =[]
    for chunk in s:
        yield chunk.strip()

#result = [chunk for chunk in result if chunk.startswith(u'但是')] 可转化为下面的函数
def startswith_filter(s):
    result = []
    for chunk in s:
        if chunk.startswith(u'但是'):
            result.append(chunk)
    return result



def startswith_filter1(s):
    result = []
    for chunk in s:
        if chunk.startswith(u'但是'):
            yield chunk

result = strip_map(result)
result = startswith_filter(result):

def split_and_extand(sep, chunks):
        result = []
        for chunk in chunks:
                result.extend(chunk.split(sep))
        return result
    
def   split_and_extand1(sep, chunks):
    result = []
    for chunk in chunks:
        
        result.extend(chunk.split(sep))
    return result
    
##############################

def splits(s, seps):
        result = [s,]
        for i in seps:
                result = split_and_extand(i, result)
        return result








