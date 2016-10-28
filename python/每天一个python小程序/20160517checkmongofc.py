#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-17
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import pymongo
import json
import time
import socket
import requests

ts=int(time.time())
hostname=socket.gethostname()

def mongo_connection_show(ip,db):
        client=pymongo.MongoClient(ip,27018)
        db=client.db
        conn=db.user_solution_impression999
        #id = long(int(id))
        #print id
        return conn.count()
        #print count
        #conn.close()



def main():
    count=mongo_connection_show('192.168.32.170','unionfc')
    count1=mongo_connection_show('192.168.32.4','unionfc-online')
    payload=[
           {
            "endpoint": hostname,
               "metric": "mongo-unionfc-count",
            "timestamp": ts,
            "step": 60,
            "value": count,
            "counterType": "GAUGE",
            "tags": "%",
           },
        ]

    payload1=[
           {
                "endpoint": hostname,
                "metric": "mongo-fc-count",
                "timestamp": ts,
                "step": 60,
                "value": count1,
                "counterType": "GAUGE",
                "tags": "%",
           },
        ]



    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload1))

if __name__ == '__main__':
    main()
