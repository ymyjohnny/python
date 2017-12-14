#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年9月5日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import datetime
import csv
import os
from sendmail1 import *


def get_campaign_id(date):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    count =  cursor.execute("SELECT  typeid  FROM  bidder_report._statsstandard  WHERE  day =  '%s'  AND  typename = 'A' AND  Location =  '' AND  typeid LIKE  '6000%%'"  % date )
    info = cursor.fetchmany(count)
    return  info
    
def get_order_id(campaign_id):
    conn=MySQLdb.connect(host="192.168.32.4",user="root",passwd="uqcqa8zd",db="dsp")
    cursor = conn.cursor ()
    cursor.execute("SELECT order_id FROM dsp_solutions WHERE group_id = '%s' GROUP BY order_id"  % campaign_id )
    t = cursor.fetchall()
    info = (j for i in t for j in i)
    return info

def get_order_id_data(order_id,date):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    sql = "SELECT  typeid,shows,clicks  FROM  bidder_report._statsstandard  WHERE  day =  '%s'  AND  typename = 'O' AND typeid = '%s' AND  Location =  '' AND  typeid like '5000%%'" % (date,order_id)
    cursor.execute(sql)
    info = cursor.fetchone()
    return info

def main():
    list = []
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(days=1)
    date = d2.strftime("%Y-%m-%d")
    sub = "%s 订单报表" % date
    f = open('dsp_report.txt','a')
    for campaign_id in get_campaign_id(date):
        list.append(campaign_id)
        for order_id in get_order_id(campaign_id):
            data = get_order_id_data(order_id,date)
            if not data:
                continue
            list.append(data)
            print list

    csvfile = file('date.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['orderid', 'show', 'click'])
    writer.writerows(list)
    csvfile.close()
    fw = "csv下载地址:http://192.168.32.4/reporttmp/%s.csv \n" % date
    f.write(fw)
    f.close()
    os.popen("mv date.csv /var/www/dosight/reporttmp/%s.csv" % date)

    f1 = open('dsp_report.txt','r')
    if len(f1.read()) != 0:
        f1.seek(0) #文件指针重新回到文件开头，重读文件
        if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
            print "done!"
        else:
             print "failed!"
    else:
      print "no data"
    f1.close()

    os.remove('dsp_report.txt')

if __name__ == '__main__':
    main()
