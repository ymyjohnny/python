#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年9月28日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import datetime,time
import os
import sys
import MySQLdb

if len(sys.argv) <= 1 or sys.argv[1] == '--help':
    print ''
    print 'Usage: ' + sys.argv[0] + ' [-t baidu  (填写渠道)] [-s 400001234 400001111 (填写投放id，空格分割)] '
    print ''
    print 'eg：python  check_winnotice_bidder_time  -t tencent -s 400001903 400001904'
    sys.exit(0)

argi = 1
logtypes = ['c','s']

if os.path.isfile('uids'):
    os.remove('uids')
f = open('uids','a')

if sys.argv[argi] == '-t':
    adx = sys.argv[argi+1]
    argi += 2
if sys.argv[argi] == '-s':
    solutionids = sys.argv[argi+1:]

ts = int(time.time())


def datetime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

def timestamp_datetime(value):
    fmt = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(fmt, value)
    return dt

def insert_mysql(solutionid,biddertime,wintime,difftime,date):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cur = conn.cursor()
    sql_content = "insert into bidder_report.bidder_win_differtime values (%s,'%s','%s',%s,'%s')" % (solutionid,biddertime,wintime,difftime,date)
    cur.execute(sql_content)
    conn.commit()

def parse_log(adx,solutionids):
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    d2 = d1 - datetime.timedelta(days=1)
    date = d2.strftime("%Y-%m-%d")
    datestr = str(d2.strftime("%Y-%m-%d"))
    os.chdir("/data/algorithm/log/%s-win-notice" % adx)
    for solutionid in solutionids: 
        Process = os.popen("grep -h solutionID=%s log4j.log.%s*" % (solutionid,datestr)).readlines()
        for i in Process:
            try:
                wintime = i.splitlines()[0].split(" INFO")[0]
                wintime_unix = datetime_timestamp(wintime)
                biddertime = int(i.splitlines()[0].split("verify_timestamp=")[1].split(",")[0][0:10])
                biddertime_dt = timestamp_datetime(biddertime)
                differtime = wintime_unix - biddertime
#            if differtime < 60:
#                print str(differtime) + 's'
#            elif  3600>differtime>60:
#                differtime = str(differtime / 60) + 'm'
#                print differtime
#            elif  86400>differtime>3600:
#                differtime = str(differtime / 3600) + 'h'
#                print differtime
#            else:
#                differtime = str(differtime / 86400) + 'd'
#                print differtime
                insert_mysql(int(solutionid),biddertime_dt,wintime,differtime,date)

            except:
                continue

def main():
    parse_log(adx,solutionids)

if __name__ == '__main__':
    main()