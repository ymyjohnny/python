#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''

import os
cpu = []

cpuinfo = os.popen('cat /proc/cpuinfo').read()
#print cpuinfo.splitlines()
for i in cpuinfo.splitlines():
    if 'processor'  in i:
        cpunumber =  int(i.split(':')[1])
        cpu.append(cpunumber+1)
print cpu[-1]





