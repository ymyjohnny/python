#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''
import os
mem = os.popen('ps aux').read()

su = 0
for i in mem.splitlines():
    if 'RSS'  in i:
        continue
    if  'chromium'  in i:
        su +=  int(i.split()[5])
print su