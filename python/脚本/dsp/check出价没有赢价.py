#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-15
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb,pymongo
import datetime
#from sendmail import *


def get_solutionid(date1,date):
    conn=MySQLdb.connect(host="221.228.228.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    #打印多少条记录
    #print date
    #print date1
    sidrow =  cursor.execute(" SELECT solutionid, sum( pass_price ) AS price FROM solution_monitors WHERE dateline >= '%s' AND dateline < '%s' GROUP BY solutionid HAVING price >100 "  % (date,date1)  )
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

def mongo_connection_show(day,sid):
        client=pymongo.MongoClient('221.228.228.4',27018)
        db=client.sdb
        conn=db.daily_sum
        #id = long(int(id))
        f = open('mail1.txt','a')
        if conn.find({"date":day,'id':sid}).count()==0:
            fw = "%s  price次数大于1000 没有赢价  \n" % sid
            f.write(fw)
        else:
            for i in  conn.find({"date":day,'id':sid}):
                yield i
        f.close()

def mongo_show(row,keys):
    for item in row:
        return item[keys]

def mysql_price(date1,date,sid):
    conn=MySQLdb.connect(host="221.228.228.46",user="root",passwd="uqcqa8zd",db="bidder_report")
    cursor = conn.cursor ()
    pricerow =  cursor.execute(" SELECT sum( pass_price ) FROM  solution_monitors WHERE solutionid = %s  AND  dateline  >= '%s'  and  dateline  <  '%s' "  % (sid,date,date1)  )
    price = cursor.fetchmany(pricerow)
    for i in price:
        mysqlprice =  i[0]
        print "mysqlprice %s "  % mysqlprice
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
    sids = get_solutionid(date1,date)
    #sub = "%s  有出价没赢价" % day
    for sid in sids:
        #print id
        show = 'show'
        mongorow = mongo_connection_show(day,sid)
        mongo_show(mongorow,show)

#    if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
#        print "done!"
#    else:
#        print "failed!"
#    f1.close()
    #os.remove('mail1.txt')



if __name__ == '__main__':
    main()
