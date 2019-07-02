#!/usr/bin/python
#coding=utf-8
# @Author: ymy
# @Date:   2019-03-27 10:08:53
# @Last Modified by:   ymy
# @Last Modified time: 2019-05-29 14:32:15


import datetime
import os
import time
import socket
import MySQLdb
import datetime
import os
import urlparse

ts = int(time.time())
hostname = socket.gethostname()



def grep_log_into_mysql(adx):
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M")
    d2 = d1 - datetime.timedelta(days=1)
    d3 = d1 - datetime.timedelta(hours=1)
    date = str(d2.strftime("%Y-%m-%d"))
    date1 = str(d3.strftime("%Y-%m-%d-%H"))
    print date1
    PS = os.popen('ps -ef |grep %s-win-notice.config|grep rtb.winnotice|grep -v grep |wc -l' % adx ).read()
    if int(PS) ==1:
        f = os.popen('grep -h WIN_REDIRECTION_INTERRUPT /data/algorithm/log/%s-win-notice/log4j.log.%s' % (adx,date1)).readlines()
        conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
        cursor = conn.cursor()
        for i in f:
            sid = i.split(' ')[6]
            cookieType = i.split(' ')[8]
            cookie = i.split(' ')[10].replace('\n','')
            sql = "insert into solution_day_win_redirection_interrupt_report(adx,day,sid,cookietype,cookie) values ('%s','%s',%s,'%s',%s,'%s')" % (adx,date,sid,cookieType,cookie,hostname)
            #print sql
            cursor.execute(sql)
            conn.commit()
        conn.close()

    else:
        Process = '-2\n'
        return Process



def main():
    adxitem = ["baidu","taobao","iqiyi","youku","tencent","adinall"]
    for adx in adxitem:    
        try:
            grep_log_into_mysql(adx)
        except:
            continue

if __name__ == '__main__':
    main()

