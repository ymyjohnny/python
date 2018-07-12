#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年12月29日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import datetime
import os
import time
import pymongo

ts = int(time.time())

def import_uid_to_mongo():
        client=pymongo.MongoClient("10.21.10.101",27018)
        db=client.win_retargetting.data
        uid = 123
        orderid = 222
        logtype = 333
        db.update_many({'uid':uid,'orderid':orderid},{'$set':{"logtype":logtype}}, upsert=True)

def main():
    import_uid_to_mongo()

if __name__ == '__main__':
    main()
