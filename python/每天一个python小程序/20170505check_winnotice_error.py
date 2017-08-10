#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-5-5
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import datetime
import os
import json
import time
import socket
import requests
import pymongo

ts = int(time.time())
hostname = socket.gethostname()
ipnum = int(hostname.split('wx')[1].split('.')[0])

def  grep_error(adx):
    grepitems = ["ERROR parse request error"]
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M")
    d2 = d1 - datetime.timedelta(minutes=1)
    date = d2.strftime("%Y-%m-%d %H:%M")
    dic = {}
    for i in grepitems:
        Process = os.popen('grep %s /data/algorithm/log/%s-win-notice/log4j.log|grep %s |wc -l' % (i,adx,date)).readlines()
        dic.setdefault(i,Process)
    return dic

def import_mongo(adx):
    client=pymongo.MongoClient("192.168.32.4",27018)
    db=client.win_error_parse_sid
    conn=db.daily
    grepitems = ["ERROR parse request error"]
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    d2 = d1 - datetime.timedelta(minutes=1)
    date = d2.strftime("%Y-%m-%d")
    #dic_mongo = {}
    for i in grepitems:
        Process = os.popen('grep %s /data/algorithm/log/%s-win-notice/log4j.log|grep %s |awk -F l= \'{print $2}\'|awk -F \& \'{print $1}\'|sort -n|uniq -c' % (i,adx,date)).readlines( )
        count = Process[0]
        sid = Process[1]
        conn.update({'sid':sid,'day':date ,'count':count},{'$set':{'sid':sid},'$set':{'day':date},'$set':{'count':count}},upsert=True)
        
    

    

def payload_process(count,metric):
        payload=[
           {
            "endpoint": hostname,
            "metric": metric,
            "timestamp": ts,
            "step": 60,
            "value": count,
            "counterType": "GAUGE",
            "tags": "%",
           },
        ]
        #requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        print payload

def main():
    adxitem = ["baidu","taobao","google","miaozhen","gdt","iqiyi","letv","sohu","youku","tencent"]
    for adx in adxitem:
        import_mongo(adx)
        grepitem = grep_error(adx)
        for k,v in grepitem.items():
            error = k.replace(' ','_')
            metric = adx + "_winnotice" + error
            count = v
            try:
                payload_process(count,metric)
            except:
                continue



if __name__ == '__main__':
    main()