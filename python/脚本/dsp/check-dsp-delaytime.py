#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-4-10
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import MySQLdb
import datetime
import os
from sendmail import *


def getdelaytime(date,monitorfield,monitorinfo):
    conn=MySQLdb.connect(host="192.168.32.4",user="root",passwd="uqcqa8zd",db="dsp_backend")
    cursor = conn.cursor ()
    #打印多少条记录
    data = cursor.execute("SELECT monitorfield,monitorcount,time,hostname FROM  `dsp_solution_statistic` WHERE  `monitorField`  =  '%s' AND TIME >=  '%s' order by monitorcount desc limit 1"  % (monitorfield,date)  )
    #打印具体内容
    info  = cursor.fetchmany(data)
    for row in info:
        monitorcount =  row[1]
        hostname = row[3]
        times = row[2]
        time = 60
        #监控延迟大于60ms
        if monitorcount > time:
           # print date, monitorfield, hostname  , monitorcount  , 'ms'  ,'大于100ms'
            f = open('delaytimemail.txt','a')
            fw = "%s %s 98%%延迟时间 %s ms 大于 %s ms %s  \n" % (times,monitorinfo,monitorcount,time,hostname)
           # print fw
            f.write(fw)
            f.close()

    cursor.close ()
    conn.close ()


def main():
    day = datetime.datetime.today().strftime("%Y-%m-%d")
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(minutes=10)
    date = d2.strftime("%Y-%m-%d %H:%M:%S")
    fielddata = {"time-adsameCookieGet-percentile98" :"redis响应时间",
             "time-apply-percentile98" : "readFC服务内部处理时间",
             "time-assessByStrategy-percentile98" : "智能竞价策略执行时间",
             "time-commit-percentile98" : "writeFC服务内部处理时间",
             "time-frequency-percentile98" : "bidder访问FC响应时间",
             "time-readmongo-percentile98" : "mongo读响应时间",
             "time-retargeting-percentile98" : "重定向服务响应时间",
             "time-setDatacache-percentile98" : "上下文写入kafka时间",
             "time-split-percentile98" : "硬过滤处理时间",
             "time-targetingStrategy-percentile98" : "人群定向相应时间",
             "time-total-percentile98" : "总响应时间"
             }
    field = fielddata.items()
    for monitorfield,monitorinfo in field:
        getdelaytime(date,monitorfield,monitorinfo)

    sub = "%s  monitorfield 98%% delay-times" % day
    try:
      f1 = open('delaytimemail.txt')
      if len(f1.read()) != 0:
        #文件指针重新回到文件开头，重读文件
        f1.seek(0)
        #邮件主题和邮件内容
        if send_mail(mailto_list,sub,f1.read()):
             print "done!"
        else:
          print "failed!"
      else:
        print "no data"
      f1.close()
    except Exception:
        return Exception

    os.remove('delaytimemail.txt')

if __name__ == '__main__':
    main()
