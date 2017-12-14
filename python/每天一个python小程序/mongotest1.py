#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年8月10日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import pymongo
import datetime

client=pymongo.MongoClient("192.168.32.140",27018)
db=client.ta_device.device_info

d1 = datetime.datetime.now()
d1.strftime("%Y-%m-%d %H:%M:%S")
d3 = d1 - datetime.timedelta(days=2)
date = d3.strftime("%Y-%m-%d ")
db.find({"update_time":{'$gt':date}})