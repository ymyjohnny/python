#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-15
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb,pymongo
import datetime
import os
from sendmail import *


def get_solutionid(date1,date):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    #打印多少条记录
    #print date
    #print date1
    sidrow =  cursor.execute(" SELECT solutionid, sum( pass_price ) AS price FROM solution_monitors WHERE dateline >= '%s' AND dateline < '%s' GROUP BY solutionid HAVING price > 1000 "  % (date,date1)  )
    #print sidrow
    #print count
    #打印具体内容
    sids = cursor.fetchmany(sidrow)
    for i in sids:
        sid =  i[0]
        #print "sid %s "  % sid
        yield  sid

    cursor.close ()
    conn.close ()
#
#打印一行，每执行1次，会向下移一行
#row = cursor.fetchone ()[2]
#print row

def mongo_connection_show(day,id):
        client=pymongo.MongoClient('192.168.32.4',27018)
        db=client.sdb
        conn=db.daily_sum
        #id = long(int(id))
        f = open('mail1.txt','a')
        if conn.find({"date":day,'id':id}).count()==0:
            # print "%s not win" % id
            fw = "%s  price次数大于1000 没有赢价,请检查投放  \n" % id
            # print fw
            f.write(fw)
        else:
            for i in  conn.find({"date":day,'id':id}):
                yield i
        f.close()

def mongo_show(row,keys):
    for item in row:
        try:
            return item[keys]
        except Exception:
            continue
            return Exception


def mysql_price(date1,date,id):
    conn=MySQLdb.connect(host="192.168.32.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    pricerow =  cursor.execute(" SELECT sum( pass_price ) FROM  solution_monitors WHERE solutionid = %s  AND  dateline  >= '%s'  and  dateline  <  '%s' "  % (id,date,date1)  )
    price = cursor.fetchmany(pricerow)
    for i in price:
        mysqlprice =  i[0]
        #print "mysqlprice %s "  % mysqlprice
        cursor.close ()
        conn.close ()
        return  mysqlprice

def main():
    #os.remove('mail1.txt')
    day = datetime.datetime.today().strftime("%Y-%m-%d")
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    date1 = today + oneday
    date = datetime.datetime.now().strftime("%Y-%m-%d ")
    sid = get_solutionid(date1,date)
    sub = "%s  有出价没赢价" % day
    for id in sid:
        #print id
        show = 'show'
        mongorow = mongo_connection_show(day,id)
        mongo_show(mongorow,show)

    f1 = open('mail1.txt')
    #for i in f1.read():
    #   print i
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
    os.remove('mail1.txt')

if __name__ == '__main__':
    main()
