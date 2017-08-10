#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-6-2
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import datetime
import os
import json
import time
import socket
import requests

ts = int(time.time())
hostname = socket.gethostname()

def grep_visit(adx,visit):
    d1 = datetime.datetime.now()
    date = d1.strftime("%Y-%m-%d %H:%M:%S")
    PS = os.popen('ps -ef |grep %s-bidder.config|grep rtb-bidder|grep -v grep|wc -l' % adx ).read()
    if int(PS) ==1:
        Process = os.popen('grep "%s" /data/algorithm/log/%s-bidder/%s.log|wc -l' % (date,adx,visit)).read()
        return Process
    else:
        Process = '0\n'
        return Process


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
        requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        #print payload

def for_adx(logtype):
    adxitem = ["baidu","taobao","google","miaozhen","gdt","iqiyi","letv","sohu","youku","tencent"]
    for adx in adxitem:
        count = grep_visit(adx,logtype).replace('\n','')
        metric = adx + "_%s_qps" % logtype
        try:
            payload_process(count,metric)
        except:
            continue


def main():
    for_adx("visit")
    for_adx("mobile")

if __name__ == '__main__':
    main()
