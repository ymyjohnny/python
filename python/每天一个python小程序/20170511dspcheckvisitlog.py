#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-5-11
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

def grep_visit(adx):
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M")
    d2 = d1 - datetime.timedelta(minutes=60)
    date = str(d2.strftime("%Y-%m-%d-%H"))
    PS = os.popen('ps -ef |grep %s-bidder.config|grep rtb-bidder|grep -v grep|wc -l' % adx ).read()
    if int(PS) ==1:
        Process = os.popen('ls /data/algorithm/log/%s-bidder/request.log.%s |wc -l' % (adx,date)).read()
        return Process
    else:
        Process = '1\n'
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

def main():
    adxitem = ["baidu","taobao","google","miaozhen","gdt","iqiyi","letv","sohu","youku","tencent"]
    for adx in adxitem:
        count = grep_visit(adx).replace('\n','')
        metric = adx + "_bidder_request_status"
        try:
            payload_process(count,metric)
        except:
            continue

if __name__ == '__main__':
    main()
