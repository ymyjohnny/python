#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-24
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import json
import pymongo
import datetime

f = open('config20151124.json', 'r')
config = json.load(f)

#字典中添加当前时间
config["datetime"] =  datetime.datetime.now().strftime("%Y-%m-%d")

#print config

#连接mongo后写入ymytest.test1表中
mongoclient = pymongo.MongoClient('221.228.230.172', 27018)
db = mongoclient.ymytest 

db.test1.save(config)

f.close()




