#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''


def isPalindrome1(s):
 for i in range(len(s))/2:
   print s
   if not s[i] == s[len(s)-i-1]:
     return False
     return True
s = [1,2,3,4,5] 
isPalindrome1(s)

def isPalindrome2(s):
  return s == s[::-1]