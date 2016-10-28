#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''
##用json输出
import csv
import tarfile
from ConfigParser  import SafeConfigParser

cfg = SafeConfigParser()
cfg.read('namesize.ini')

# fname = cfg.get('sec','package')
# cname = cfg.get('sec','csvname')

f = tarfile.open(cfg.get('sec','package'))
fo = open(cfg.get('sec','csvname'), 'w')
writer = csv.writer(fo)
attr = cfg.get('sec','attr').split(',')
print attr

writer.writerow(attr)

result = []
for m in f.getmembers():
    result.append()
#         writer.writerow(
#                         map(lambda name: getattr(m, name), attr))
fo.close()
f.close()
