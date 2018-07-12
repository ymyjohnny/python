#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年12月13日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import datetime
import os
import urlparse


os.popen('/bin/bash parselog.sh')

def insert_mysql_impression(date,idtype):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    logdir = '/data/nginxlog/%s/%s_%s' % (date,idtype,date)
    f = open('%s' % logdir)
    idname = idtype + "id"
    for i in f.read().splitlines():
        info = i.split(",")
        solutionid = info[1] 
        show = info[2]
        sql = "insert into %s_point_show(day,%s,showcount) values ('%s',%s,%s)" % (idtype,idname,date,solutionid,show)
        cursor.execute(sql)
    conn.commit()
    conn.close()


def insert_mysql_iqiyi_pdb_impression(date):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    logdir = '/data/nginxlog/%s/iqiyi_pdb_%s' % (date,date)
    f = open('%s' % logdir)
    dt = {}
    for i in f.read().splitlines():
        urla = i.split("?")
        #分析url参数写入字典
        res = urlparse.parse_qs(urla[1]).values()
        t = res[0]
        dealid = res[1]
        #list转str
        dealid_t = "_".join(dealid + t)

        if dealid_t in dt:
            count = dt[dealid_t]
        else:
            count = 0
        count = count + 1
        dt[dealid_t] = count
    for dealidt,count in dt.items():
        dealid = dealidt.split("_")[0]
        t = dealid_t.split("_")[1]
        sql = "insert into iqiyi_pdb_notice(day,dealid,type,showcount) values ('%s',%s,%s,%s)" % (date,dealid,t,count)
        cursor.execute(sql)
    conn.commit()
    conn.close()
 

    
def main():
            d1 = datetime.datetime.now()
            d1.strftime("%Y-%m-%d %H:%M:%S")
            d2 = d1 - datetime.timedelta(days=1)
            date = d2.strftime("%Y-%m-%d")
            insert_mysql_impression(date,"solution")
            insert_mysql_impression(date,"order")
            insert_mysql_iqiyi_pdb_impression(date)

            #insert_mysql_impression(date,"campaign")
    
if __name__ == '__main__':
    main()
