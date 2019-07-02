#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年7月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month < 12:
    sum = months[month - 1]
    sum +=  day

leap = 0
#公历纪年法中：能被4整除的大多是闰年；能被100整除而不能被400整除的年份不是闰年；能被3200整除的也不是闰年；如1900年是平年，2000年是闰年，3200年不是闰年
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if  (month > 2) and (leap == 1) :
    sum += 1
print sum
