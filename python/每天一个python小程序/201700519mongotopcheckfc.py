#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-5-19
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import os
import json
import time
import socket
import requests

ts = int(time.time())
hostname = socket.gethostname()

def check_mongotop(port):
    mongotop = os.popen('mongotop --host 127.0.0.1:%s -n 1|grep unionfc|head -1|awk \'{print $2}\'|awk -F ms \'{print $1}\' ' % port ).read()
    return mongotop


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

def main():
    portlist = ["27017","27027","27037","27047","27057","27067","27077","27087","27097","27107","27117","27127"]
    for port in portlist:
        metric = "mongotop." + port
        count = check_mongotop(port).replace('\n','')
        try:
            payload_process(count,metric)
        except:
            continue

if __name__ == '__main__':
    main()
