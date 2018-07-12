#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年5月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import datetime
import os
from sendmail_html import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def get_sid_info(date):
    date1 = date + ' 00:00:00'
    date2 = date + ' 23:59:59'
    conn=MySQLdb.connect(host="192.168.32.4",user="root",passwd="uqcqa8zd",db="dsp",charset = 'utf8')
    cursor = conn.cursor ()
    sql =  "SELECT group_id,name,id AS order_id,create_time,start_time,end_time FROM dsp_orders where start_time >= '%s' and start_time <= '%s'" % (date1,date2)
    #print sql
    cursor.execute(sql)
    info = cursor.fetchall()
    return  info


def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(days=1)
    date = d2.strftime("%Y-%m-%d")
    #date = '2018-05-18'
    sub = "%s 上线订单" % date
    f = open('mail.txt','a')
    orderinfos = get_sid_info(date)
    if orderinfos:
        fw = "<div><table border><th>活动id</th><th>订单id</th><th>订单名称</th><th>创建时间</th><th>订单开始时间</th><th>订单结束时间</th>"
        for i in orderinfos:
            groupid = i[0]
            ordername = i[1]
            orderid = i[2]
            create_time = i[3]
            start_time = i[4]
            end_time = i[5]
            fw += "<tr><td><div align=right> %s </div></td><td><div align=right> %s </div></td><td><div align=right> %s </div></td><td><div align=right>%s</div></td><td><div align=right>%s</div></td><td><div align=right>%s</div></td></tr>" % (groupid,orderid,ordername,create_time,start_time,end_time)
        fw += "</table></div>"

        f.write(fw)
        f.close()
    else:
        print "no order"

    f1 = open('mail.txt','r')
    if len(f1.read()) != 0:
        f1.seek(0) #文件指针重新回到文件开头，重读文件
        if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
            print "done!"
        else:
            print "failed!"
    else:
        print "no data"
    f1.close()
    os.remove('mail.txt')
    
    
if __name__ == '__main__':
    main() 
