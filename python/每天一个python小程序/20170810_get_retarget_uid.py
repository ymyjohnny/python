#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年8月10日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import sys
import pymongo
import os
from itertools import groupby

if len(sys.argv) <= 1 or sys.argv[1] == '--help':
    print ''
    print 'Usage: ' + sys.argv[0] + ' [-t c or s (填写日志类型显示或点击，不加-t参数为所有类型)] [-o 500001234 500001111 (填写订单id，空格分割)] '
    print ''
    print 'eg：python  get_retarget_uid.py  -t c -o 500001903 500001904'
    sys.exit(0)

argi = 1
logtypes = ['c','s']

if os.path.isfile('uids'):
    os.remove('uids')
f = open('uids','a')

if sys.argv[argi] == '-t':
    #sys.argv[argi+1:] 加冒号代表传入数组，不带冒号表示传入字符串
    logtypes = sys.argv[argi+1]
    argi += 2
if sys.argv[argi] == '-o':
    orderids = sys.argv[argi+1:]

client=pymongo.MongoClient("192.168.32.140",27018)
db=client.win_retargetting.data
ls = []
for i in orderids:
    print i
    for l in logtypes:
        mongorow = db.find({"orderid":i , "logtype":l})
        for r in mongorow:
            fw =  r['uid'] + "\n"
            ls.append(fw)

            
fw = groupby(sorted(ls))
for item in fw:
    f.write(item[0])
f.close()
