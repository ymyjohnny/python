#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


import csv
import tarfile
from ConfigParser  import SafeConfigParser

cfg = SafeConfigParser()
cfg.read('namesize.ini')

# fname = cfg.get('sec','package')
# cname = cfg.get('sec','csvname')

f = tarfile.open(cfg.get('sec','package'))
fo = open(cfg.get('sec','csvname'), 'w')
attr = cfg.get('sec','attr').split(',')
print attr


writer = csv.writer(fo)

writer.writerow(attr)
for m in f.getmembers():
    writer.writerow(
                    [getattr(m, name) for name in attr])
#         writer.writerow(
#                         map(lambda name: getattr(m, name), attr))
fo.close()
f.close()


