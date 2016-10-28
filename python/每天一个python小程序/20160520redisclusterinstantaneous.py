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

ts = int(time.time())
hostname = socket.gethostname()
ipnum = int(hostname.split('wx')[1].split('.')[0])

def redis_get_info(ip,port):
    r = redis.Redis(ip,port)
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
        requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        #print payload

def main():
        for a in range(6370,6390):
            ip = '192.168.32.%d' % ipnum
            metric = 'rediscluster_instantaneous_ops_%d' % a
            port = a
            count = redis_get_info(ip,port)

            payload_process(count,metric)
            

if __name__ == '__main__':
    main()
