#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年12月1日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import datetime
import time
import requests
import json
import socket

ts = int(time.time())
hostname = socket.gethostname()



def get_sid_info(adx,adtype,date,flowtype):
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="uqcqa8zd",db="dsp_backend")
    cursor = conn.cursor ()
    sql = "SELECT * FROM  (dsp_daily_solution_winnotice  w  left join (SELECT s.id AS solutionID,s.flow_type AS flow_type,a.ad_type AS ad_type FROM (dsp.dsp_solutions s left join dsp.ad_sizes a on (s.ad_size_id = a.id) ) ) info on (w.solutionid = info.solutionID)) where time >= '%s' and ad_type = '%s' and adx = '%s' and flow_type = '%s'" % (date,adtype,adx,flowtype)
    #print sql
    cursor.execute(sql)
    info = cursor.fetchall()
    return  info

def payload_process(count,metric):
        payload=[
           {
            "endpoint": hostname,
            "metric": metric,
            "timestamp": ts,
            "step": 600,
            "value": count,
            "counterType": "GAUGE",
            "tags": "%",
           },
        ]
        requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        #print payload

def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(minutes=10)
    date = d2.strftime("%Y-%m-%d %H:%M:%S")
    #print date
    adtypes = {"FIXED":"硬广",
                            "CLIP":"视频",
                            "FEEDS":"信息流"}
    flowtypes = ["PC","Mobile-App","Mobile-Web"]
    adxes = ["taobao","baidu","youku","iqiyi","tencent","gdt","letv","sohu","quantone","adinall"]
    #print "adx","广告类型","平台","cpm单价"
    for adtype,adtypeinfo  in adtypes.items():
        #print "    "
        #print adtypeinfo,adtype
        #print  "   "
        for adx  in adxes:
            for flowtype in flowtypes:
                sid_infos = get_sid_info(adx,adtype,date,flowtype)
                if not sid_infos:
                    continue
                impression_sum = 0
                price_sum = 0
                for i in sid_infos:
                    impression = i[4]
                    price = i[3]
                    #adtype = i[8]
                    flowtype = i[7]
                    impression_sum +=  impression
                    price_sum +=  price
                    cpm = round(price_sum / impression_sum * 1000 ,2)
                #print adx,adtypeinfo,flowtype,impression_sum,cpm
                count = adx + "_" + adtype + "_" + flowtype
                print count
                payload_process(cpm,count)
                

if __name__ == '__main__':
    main()
