#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-14
@author: ymy
'''

import re

fin = open("word.txt" ,"r")
fout = open("reslut.txt","w")

str =  fin.read()

reObj=re.compile("\b?([a-zA-Z]+)\b?")
print reObj
words = reObj.findall(str)
print words

word_dict = {}

for word in words:
    if(word_dict.has_key(word)):
        word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
    else:
        word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))       
for(word,number) in word_dict.items():
    fout.write(word+":%d\n"%number)
