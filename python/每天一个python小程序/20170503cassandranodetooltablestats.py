#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-4-28
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import re
import subprocess

import json
import time
import socket
import requests


ts = int(time.time())
hostname = socket.gethostname()
ipnum = int(hostname.split('wx')[1].split('.')[0])


def tablestats(table):
    Process = subprocess.check_output(["/opt/apache-cassandra-3.0.9/bin/nodetool" ,"tablestats" ,table]).splitlines()
    dic = {}
    for line in Process:
        grepitem = ["Read Count","Read Latency","Write Count","Write Latency","Pending Flushes"]
        for s in grepitem:
            if  re.search(s, line):
                key = line.split(":")[0]
                value = line.split(":")[1].split("ms")[0]
                dic.setdefault(key,value)
    return dic



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
    tableitem = ["samedata5","samedata5_for_replication"]
    for table in tableitem:
            keyspacestat = tablestats(table).items()
            print keyspacestat
            for project,count in keyspacestat:
                a = table+"."+project.lstrip()
                metric = a.replace(' ','_')
                count = round(float(count), 2)
                #print metric.lstrip()
                try:
                  payload_process(count,metric)
                except:
                  continue


if __name__ == '__main__':
    main()
