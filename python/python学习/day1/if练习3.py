#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''
#如果你的年龄是偶数，从2开始打印知道你的年龄为止，如果是你的年龄是奇数，从1开始
age = 31
for  i in range(1,100,2):
    print i 
    if i > age - 2:
        break

