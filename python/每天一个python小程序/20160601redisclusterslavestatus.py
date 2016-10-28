#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-6-01
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
    return info['master_link_status']
      
    

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
            metric = 'rediscluster_slave_status_%d' % a
            port = a
            try:
                status = redis_get_info(ip,port)
                if status == 'up':
                    count = 1
                    payload_process(count,metric)
                else:
                    count = 0
                    payload_process(count,metric)
            except:
                continue
            

if __name__ == '__main__':
    main()
