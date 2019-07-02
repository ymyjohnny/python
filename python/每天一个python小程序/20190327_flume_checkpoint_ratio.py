#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ymy
# @Date:   2019-03-27 10:08:53
# @Last Modified by:   ymy
# @Last Modified time: 2019-03-27 11:34:51


import MySQLdb
import datetime
import os
import socket
import json
import time
import requests


ts=int(time.time())
hostname=socket.gethostname()
d1 = datetime.datetime.now()
d1.strftime("%Y-%m-%d")
d2 = d1 - datetime.timedelta(hours=1)
#d2 = d1 - datetime.timedelta(days=1)
date = str(d2.strftime("%Y-%m-%d"))

def get_mysql(hostname,date):
    conn=MySQLdb.connect(host="mycat192.adsame.com",user="samedata",passwd="Samedata170!",db="samedata_backend",charset = 'utf8')
    cursor = conn.cursor ()
    sql = " SELECT * FROM  checkpoint_statistics where host = '%s' and date = '%s'" % (hostname,date)
    #print sql
    info = cursor.fetchmany(cursor.execute(sql))
    for i in info:
        passes = i[4]
        filter = i[3]
        metric = i[2]
        if filter > 10000:
            filter_ratio = round(float(filter) / (int(filter) + int(passes)),2)
            #print metric + str(filter_ratio)

            payload=[
               {
                "endpoint": hostname,
                "metric": metric,
                "timestamp": ts,
                "step": 60,
                "value": filter_ratio,
                "counterType": "GAUGE",
                "tags": "%",
               },
            ]
            requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        else:
            #fliter小于10000输出一个恒定值 0.111111
            payload=[
               {
                "endpoint": hostname,
                "metric": metric,
                "timestamp": ts,
                "step": 60,
                "value": 0.111111,
                "counterType": "GAUGE",
                "tags": "%",
               },
            ]
            requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))


def main():
    get_mysql(hostname,date)

if __name__ == '__main__':
    main()
