#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''
##从config文件导入tar包名，取出tar包中文件的文件名和size，把这些信息输入到csv文件里，csv文件名从config文件里取

#import ConfigParser
import csv
import tarfile
from ConfigParser  import SafeConfigParser

cfg = SafeConfigParser()
cfg.read('namesize.ini')

# fname = cfg.get('sec','package')
# cname = cfg.get('sec','csvname')

f = tarfile.open(cfg.get('sec','package'))
fo = open(cfg.get('sec','csvname'), 'w')
f1 = cfg.get('sec','attr')



writer = csv.writer(fo)
for m in f.getmembers():
        writer.writerow((m.name, m.size))
fo.close()
f.close()



# def tar1(s):
#     f = tarfile.open(s)
#     for m in f.getmembers():
#         print m.name, m.size
#         
# tar1(fname)

# def csv1(a):
#     with open('a', 'wb') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)





    