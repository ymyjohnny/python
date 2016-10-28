#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


def startswith_filter1(s):
    result = []
    for chunk in s:
        if chunk.startswith(u'但是'):
            yield chunk