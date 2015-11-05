#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-1
@author: ymy
'''


import re
r = re.compile('.'.join(['\d{1,3}' ,]*4))
#r = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}') 和上面一行一样

r.search('114.114.114.114  8.8.8.8').group(0)



url = '13.43.33.44fhdir44.32.52.23'
print url

#字符串里取出ip地址
# re.split('[a-z]+', '13.43.33.44fhdiD44.32.52.23', flags=re.IGNORECASE)
# ['13.43.33.44', '44.32.52.23']

print re.split('[a-z]+', url, flags=re.IGNORECASE)
