#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ymy
# @Date:   2019-03-15 10:43:53
# @Last Modified by:   ymy
# @Last Modified time: 2019-04-29 14:43:36
import MySQLdb
import datetime
import os
import socket
hostname = socket.gethostname()
def Processlog(logname):
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    #d2 = d1 - datetime.timedelta(days=1)
    d2 = d1 - datetime.timedelta(hours=1)
    d3 = d1 - datetime.timedelta(days=7)
    date = str(d2.strftime("%Y-%m-%d"))
    date_file = str(d2.strftime("%Y-%m-%d-%H"))
    print date
    date_del = str(d3.strftime("%Y-%m-%d"))
    PS = os.popen(" ps -ef |egrep 'local-dsp-unionid2samedata.conf|local-adv2samedata.conf|remote-adv2samedata.conf' |grep -v grep|wc -l" ).read()
    if int(PS) ==1:
        conn=MySQLdb.connect(host="GETFLUMELOGTOMYSQLADDR",user="samedata",passwd="Samedata170!",db="samedata_backend",charset = 'utf8')
    #conn=MySQLdb.connect(host="dsptest.mysql.adsame.com",user="samedata",passwd="Samedata170!",db="samedata_backend_test",charset = 'utf8')
        cursor = conn.cursor ()
        try:
            if logname == "device":
                Process = os.popen("awk -F brand\=  '{print $2}' /data/algorithm/log/local-dsp-unionid2samedata/%s.log.%s|grep -v '�'" % (logname,date_file)).read().splitlines()
                for i in Process:
                    data = MySQLdb.escape_string("brand=" + i.split(", filter")[0])
                    filter = i.split(", filter")[1].split(', ')[0]
                    passes = i.split(", pass")[1]
                    sql = "insert into %s_statistics(date,host,%s,filter,pass) values('%s','%s','%s','%s','%s') on duplicate key update filter = filter + %s, pass = pass + %s" % (logname,logname,date,hostname,data,filter,passes,filter,passes)
                    cursor.execute(sql)
            else:
                #Process = os.popen("awk -F \) '{print $2}' /data/algorithm/log/local-dsp-unionid2samedata/%s.log.%s-*" % (logname,date)).read().splitlines()
                Process = os.popen("awk -F \) '{print $2}' /data/algorithm/log/local-dsp-unionid2samedata/%s.log.%s" % (logname,date_file)).read().splitlines()
                for i in Process:
                    data = MySQLdb.escape_string(i.split(", filter")[0])
                    filter = i.split(", filter")[1].split(', ')[0]
                    passes = i.split(", pass")[1]
                    sql = "insert into %s_statistics(date,host,%s,filter,pass) values('%s','%s','%s','%s','%s') on duplicate key update filter = filter + %s, pass = pass + %s" % (logname,logname,date,hostname,data,filter,passes,filter,passes)
                    cursor.execute(sql)
        except Exception, e:
            print 'str(Exception):\t', e.message
        conn.commit()
        #删除过期数据
        #delsql = "delete FROM %s_statistics WHERE date = '%s'" % (logname,date_del)
        #cursor.execute(delsql)
        #优化表
        #optimizesql = "OPTIMIZE TABLE  %s_statistics" % logname
        #cursor.execute(optimizesql)
        #提交sql
        #conn.commit()
        cursor.close()
    else:
        Process = '0\n'
        print Process
def main():
    #lognames = ["device","checkpoint"]
    lognames = ["app","device","checkpoint","domain"]
    for logname in lognames:
       Processlog(logname)
if __name__ == '__main__':
    main()
