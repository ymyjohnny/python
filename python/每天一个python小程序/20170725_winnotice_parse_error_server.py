#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年7月25日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import datetime

import pymongo
import os
from sendmail import *

def mongo_connection_show(date):
        client=pymongo.MongoClient('192.168.32.4',27018)
        db=client.win_error_parse_sid
        conn=db.daily
        mongorow = conn.find({'count':{'$gt':10000},'date':date})
        return  mongorow

     
def main():
        d1 = datetime.datetime.now()
        d1.strftime("%Y-%m-%d")
        d2 = d1 - datetime.timedelta(minutes=60)
        date = str(d2.strftime("%Y-%m-%d-%H"))
        items = mongo_connection_show(date)
        if items.count() != 0:
          sub = "%s winnotice_error_parse_sid" % date
          f = open('mail.txt','a')
          f.write("winnotice每小时解析错误超过10000的投放如下:\n")
          for i in items:
              #print i
              sid = i['sid']
              count = i['count']
              date1 = i['date']
              fw = "投放id :%s   时间:%s  错误数: %s  \n" % (sid,date1,count)
              f.write(fw)
          f.close()
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
        else:
          print 'none'
            
if __name__ == '__main__':
    main()
