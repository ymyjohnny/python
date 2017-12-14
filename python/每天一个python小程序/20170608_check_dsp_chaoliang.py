#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-6-8
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb,pymongo
import datetime
import os
from sendmail import *


def get_order_impression(date):
    conn=MySQLdb.connect(host="192.168.32.4",user="root",passwd="uqcqa8zd",db="dsp")
    cursor = conn.cursor ()
    #打印多少条记录
    #count =  cursor.execute("SELECT  order_id,impression FROM  dsp.dsp_date_configs WHERE date =  '%s' AND solution_id = 0 AND order_id in (SELECT id FROM dsp.dsp_orders where status in ('1','2','6','5','7') ) "  % date )
    count =  cursor.execute("SELECT  order_id,sum(impression) AS impression,status FROM  dsp.dsp_date_configs daily  left join dsp.dsp_orders o on (o.id = daily.order_id)  WHERE date =  '%s' AND solution_id = 0 group by order_id"  % date )
    info = cursor.fetchmany(count)
    dict = {}
    for i in info:
        orderid =  i[0]
        impression = i[1] 
        status = i[2]
        dict.setdefault(orderid,[impression,status])
    return dict
    cursor.close ()  
    conn.close ()  


def get_mongo_expression(date,orderid):
        client=pymongo.MongoClient('192.168.32.4',27018)
        db=client.gdb
        conn=db.daily_sum
        #id = long(int(id))
        #print id
        for i in  conn.find({"date":date,'id':orderid}):
            yield i
        conn.close()

def mongo_show(row,keys):
    for item in row:
        return item[keys]


def sendmail(sub):
    sub = sub
    f1 = open('mail_chao.txt','r')
    if len(f1.read()) != 0:
      #print len(f1.read())
      f1.seek(0) #文件指针重新回到文件开头，重读文件

      if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
         print "done!"
      else:
         print "failed!"
    else:
      print "no data"
    f1.close()
    os.remove('mail_chao.txt')


def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(minutes=1440)
    date = d2.strftime("%Y-%m-%d")
    f = open('mail_chao.txt','a')
    dict = get_order_impression(date)
    mongoshowsum = 0    
    impressionsum = 0
    for orderid,[impression,status] in dict.items():
        if impression == 0:
           continue
        mongorow = get_mongo_expression(date,orderid)
        try:
            mongoshow = int(mongo_show(mongorow,'show'))
        except:
            impression = 0
            mongoshow = 0
            #print orderid,impression,mongoshow
            continue
        if status == '2' and mongoshow < 100 and impression == 0:
            impression = 0
            mongoshow = 0
        mongoshowsum += mongoshow
        impressionsum += impression
        baifen = ((mongoshow) - float(impression)) / int(impression)
        baifenround = round(baifen,2) *100
        if baifenround > 1:
          fw = "超量投放:%s 需要投放量:%s 实际投放量:%s 超出百分比: %s%% \n" % (orderid,impression,mongoshow,baifenround)
          f.write(fw)
        if status == '2' and mongoshow > 100 and mongoshow < impression :
          fw = "中途暂停:%s 需要投放量:%s 实际投放量:%s \n" % (orderid,impression,mongoshow)  
          f.write(fw)
    print mongoshowsum
    print impressionsum
    
    fw = "\n 投放需求总量:%s 实际投放总量:%s \n" % (impressionsum,mongoshowsum)
    f.write(fw)
    f.close()
    sub = "%s 投放量状态" % date
    sendmail(sub)

if __name__ == '__main__':
    main()
