#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年7月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import datetime
import os
import time
import pymongo

ts = int(time.time())

def import_mongo(adx):
    client=pymongo.MongoClient("192.168.32.61",27018)
    db=client.win_error_parse_sid.daily
    grepitems = ["ERROR\ parse\ request"]
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    d2 = d1 - datetime.timedelta(minutes=60)
    date = str(d2.strftime("%Y-%m-%d-%H"))
    #dic_mongo = {}
    for i in grepitems:
        try:
            print adx
            Process = os.popen('grep %s /data/algorithm/log/%s-win-notice/log4j.log.%s|awk -F l= \'{print $2}\'|awk -F \& \'{print $1}\'|grep -v ^$|sort -n|uniq -c|awk \'{print $1","$2}\'' % (i,adx,date)).readlines()
            #print Process
            for i in  Process:
                count = int(i.splitlines()[0].split(',')[0])
                sid = i.splitlines()[0].split(',')[1]
                db.update_many({'sid':sid,'date':date},{'$set':{"update_time":d1},'$inc':{'count':count}}, upsert=True)
        except:
            print 4444

def main():
    adxitem = ["baidu","taobao","google","miaozhen","gdt","iqiyi","letv","sohu","youku","tencent","quantone","xiaomi"]
    for adx in adxitem:
        import_mongo(adx)

if __name__ == '__main__':
    main()
