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
    
def main():
            d1 = datetime.datetime.now()
            d1.strftime("%Y-%m-%d %H:%M:%S")
            d2 = d1 - datetime.timedelta(days=1)
            date = d2.strftime("%Y-%m-%d")
            insert_mysql_impression(date,"solution")
            insert_mysql_impression(date,"order")
            #insert_mysql_impression(date,"campaign")
    
if __name__ == '__main__':
    main()
