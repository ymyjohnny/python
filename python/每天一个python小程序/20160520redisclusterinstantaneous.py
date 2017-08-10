#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-6-21
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import redis
import sys
import json
import time
import socket
import requests

#from rediscluster import RedisCluster

ts = int(time.time())
hostname = socket.gethostname()
ipnum = int(hostname.split('wx')[1].split('.')[0])

def get_redis_scan(ip, port):
    try:
        r = redis.Redis(host = ip, port = port)
        # startup_nodes = [{"host": "192.168.32.145", "port": "6379"}]
        # r = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    except Exception,e:
        print "Connect Error!"
        sys.exit(1)
    #scan = r.scan(cursor=0, match=None,count=100)[1]
    scan = r.scan(cursor=0, match=None,count=10000000)[1]
    return scan

def key_sum(k,scan):
    sm = 0
    s = 0
    list = []
    for i in scan:
        s += 1
        if k in i:
            sm  += 1
    list.append(sm)
    list.append(s)
    return list

def payload_process(count,metric):
        payload=[
           {
            "endpoint": hostname,
            "metric": metric,
            "timestamp": ts,
            "step": 3600,
            "value": count,
            "counterType": "GAUGE",
            "tags": "%",
           },
        ]
        #requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        print payload

def main():
    s = 0
    for a in range(6370,6390):
      port = a
      ip = '192.168.32.%d' % ipnum
      scan = get_redis_scan(ip, port)
      keys = ['mydmp','rtq_cookie_user','REV','FOR','throttler','samedataweb','dsp_mobile']
      for k in keys:
        metric = '%s_%s' % (k,port)
        count = key_sum(k,scan)[0]
        payload_process(count,metric)

      metric = 'redis_key_sum_%s' % port
      count = key_sum(k,scan)[1]
      payload_process(count,metric)

if __name__ == '__main__':
    main()
