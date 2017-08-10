#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-5-24
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import requests
import json
import time
import socket

ts=int(time.time())
p={"step":1,"start":ts-120}
v=requests.get("http://192.168.32.174:8888/Samedata_Cluster/cluster-metrics/DC1/key-cache-hit-rate",params=p)
res=json.loads(v.text)
hostname=socket.gethostname()
payload=[
    {
        "endpoint": hostname,
        "metric": "cassandra_key_cache_hit_rate",
        "timestamp": ts,
        "step": 60,
        "value": "%.2f" % round(res["Average"]["AVERAGE"][0][1]*100,2) ,
        "counterType": "GAUGE",
        "tags": "%",
    },

]

r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
