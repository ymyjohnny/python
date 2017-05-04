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
import os

ts = int(time.time())
hostname = socket.gethostname()
ipnum = int(hostname.split('wx')[1].split('.')[0])
files = '/tmp/cassandra_tablestatus.txt'

def tablestats(table):
    Process = subprocess.check_output(["/opt/apache-cassandra-3.0.9/bin/nodetool" ,"tablestats" ,table]).splitlines()
    dic = {}
    for line in Process:
        grepitem = ["Read Latency","Write Latency","Pending Flushes"]
        for s in grepitem:
            if  re.search(s, line):
                key = line.split(":")[0]
                value = line.split(":")[1].split("ms")[0]
                dic.setdefault(key,value)
    return dic

def tablestats_read_write(table):
    Process = subprocess.check_output(["/opt/apache-cassandra-3.0.9/bin/nodetool" ,"tablestats" ,table]).splitlines()
    dic = {}
    dic_old = {}
    f = open('/tmp/cassandra_tablestatus.txt.'+table, 'r')
    for l in f.readlines():
        k = l.split(':')[0]
        v = l.split(':')[1]
        dic_old.setdefault(k,v)
    #return dic_old
    os.remove('/tmp/cassandra_tablestatus.txt.'+table)
    for line in Process:
        grepitem = ["Read Count","Write Count"]
        for s in grepitem:
            if  re.search(s, line):
                key = line.split(":")[0]
                value_new = line.split(":")[1].split("ms")[0]
                for k,v in dic_old.items():
                    if re.search(s, k):
                        value_old = v.replace("\n","")
                        value = int((int(value_new) - int(value_old)) / 60)
                        dic.setdefault(key,value)
                        f = open('/tmp/cassandra_tablestatus.txt.'+table,'a')
                        fw = "%s : %s \n" % (key,value_new)
                        f.write(fw)
                        f.close()
    return dic

def  keyspacestat_process(keyspacestat,table):
    for project,count in keyspacestat:
        a = table+"."+project.lstrip()
        metric = a.replace(' ','_')
        count = round(float(count), 2)
        try:
            payload_process(count,metric)
        except:
            continue

def touch_base_file(files,table):
    file_object = open(files+table,'a')
    fw = "Read Count : 0 \nWrite Count : 0 \n"
    file_object.write(fw)
    file_object.close()


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
            #print keyspacestat
            keyspacestat_process(keyspacestat,table)

            if os.path.exists('/tmp/cassandra_tablestatus.txt.'+table):
                linecount = len(open('/tmp/cassandra_tablestatus.txt.'+table,'r').readlines())
                if linecount == 2 :
                    keyspacestat_rw = tablestats_read_write(table).items()
                    keyspacestat_process(keyspacestat_rw,table)
                else:
                    os.remove('/tmp/cassandra_tablestatus.txt.'+table)
                    touch_base_file(file,table)

            else:
                touch_base_file(file,table)
if __name__ == '__main__':
    main()