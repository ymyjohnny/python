#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-5-25
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import requests
import json
import time
import socket

hostname=socket.gethostname()
ts=int(time.time())
try:
    v=requests.get("http://127.0.0.1:31001/metrics")
    res=json.loads(v.text)
    baiduTagsource_EventReceivedCount=int(res["SOURCE.baiduTagSource"]["EventReceivedCount"])
    baiduTagsource_EventAcceptedCount=int(res["SOURCE.baiduTagSource"]["EventAcceptedCount"])
    baiduTagchannel_ChannelSize=int(res["CHANNEL.tagChannel"]["ChannelSize"])

    payload=[
        {
            "endpoint": hostname,
            "metric": "baiduTagsource_EventReceivedCount",
            "timestamp": ts,
            "step": 60,
            "value": baiduTagsource_EventReceivedCount,
            "counterType": "COUNTER",
            "tags": "",
        },
        {
            "endpoint": hostname,
            "metric": "baiduTagsource_EventAcceptedCount",
            "timestamp": ts,
            "step": 60,
            "value": baiduTagsource_EventAcceptedCount,
            "counterType": "COUNTER",
            "tags": "",
        },
        {
            "endpoint": hostname,
            "metric": "baiduTagchannel_ChannelSize",
            "timestamp": ts,
            "step": 60,
            "value": baiduTagchannel_ChannelSize,
            "counterType": "GAUGE",
            "tags": "",
        },

    ]
    print json.dumps(payload)
    #r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
except Exception,e:
    print e
