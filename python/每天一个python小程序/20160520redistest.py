#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-20
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import redis
import json
import time
import socket
import requests

ts=int(time.time())
hostname=socket.gethostname()


def redis_get_info(ip,port):
    r = redis.Redis('ip','port')
    info = r.info()
    return info['instantaneous_ops_per_sec']


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
    for i in range(146,150):
        for a in range(6370,6389):
            ip = '192.168.32.i'
            port = a
            count =  redis_get_info(ip,port)
            metric = 'wx%d.adsame.com redis-cluster%d'   %(i,a)
            payload_process(count,metric)
            



if __name__ == '__main__':
    main()
