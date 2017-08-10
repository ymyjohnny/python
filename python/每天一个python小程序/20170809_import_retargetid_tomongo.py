#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年8月9日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import datetime
import os
import time
import pymongo

ts = int(time.time())

def import_uid_to_mongo():
    client=pymongo.MongoClient("192.168.50.4",27018)
    db=client.win_retargetting.data
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    d2 = d1 - datetime.timedelta(days=1)
    date = str(d2.strftime("%Y-%m-%d"))
    os.chdir("/home/samelog/backup")
    Process = os.popen("awk -F \, '{print $1,$5,$12}' bidder_report.%s.*|sort -n|uniq"   % date  ).readlines()
    for i in Process:
        try:
           logtype =  i.splitlines()[0].split()[0]
           uid = i.splitlines()[0].split()[1]
           orderid  = i.splitlines()[0].split()[2]
           if len(uid) == 15:
              try:
                  d3 = datetime.datetime.now()
                  f = float(uid)
                  #print uid  + "," + orderid + "," + logtype
                  db.update_many({'uid':uid,'orderid':orderid, 'logtype':logtype},{'$set':{"update_time":d3}}, upsert=True)
              except:
                  continue
        except:
              continue

def main():
    import_uid_to_mongo()

if __name__ == '__main__':
    main()
