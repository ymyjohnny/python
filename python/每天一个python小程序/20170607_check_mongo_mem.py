#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-6-7
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

def check_mongomem(port):
    mem = os.popen('ps aux').read()
    for i in mem.splitlines():
        if 'RSS' in i:
            continue
        if 'replSet' not in i:
            continue
        if port in i:
            mongomemp = int(i.split()[5]) * 1000
            return mongomemp


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
    portlist = ["27017","27027","27037","27047","27057","27067","27077","27087","27097","27107","27117","27127"]
    #mem = int(os.popen('free|grep Mem|awk \'{print $2}\' ').read())
    for port in portlist:
        metric = "mongomem." + port
        count = check_mongomem(port)
        try:
            payload_process(count,metric)
        except:
            continue

if __name__ == '__main__':
    main()
