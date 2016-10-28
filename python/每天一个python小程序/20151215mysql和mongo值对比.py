#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-15
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb,pymongo
import datetime


#.strftime("%Y-%m-%d")
#datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print datetime

def get_solutionid(date):
    conn=MySQLdb.connect(host="111.111.111.111",user="ymy",passwd="111111",db="test")
    cursor = conn.cursor ()
    #打印多少条记录
    count =  cursor.execute("SELECT * FROM `dsp_daily_solution_winnotice` where time >= '%s'  group by solutionid"  % date )
    #print count
    #打印具体内容
    info = cursor.fetchmany(count)
    for i in info:
        mysqlsid =  i[0]
        yield mysqlsid

    cursor.close ()  
    conn.close ()  
#     
#打印一行，每执行1次，会向下移一行
#row = cursor.fetchone ()[2]
#print row

def mongo_connection_show(day,id):
        client=pymongo.MongoClient('111.111.111.111',27018)
        db=client.sdb
        conn=db.daily_sum
        #id = long(int(id))
        #print id
        for i in  conn.find({"date":day,'id':id}):
            yield i
        conn.close()

def mongo_show(row,keys):
    for item in row:
        return item[keys]
        
def mysql_show(date,id):
    conn=MySQLdb.connect(host="111.111.111.111",user="ymy",passwd="111111",db="test")
    cursor = conn.cursor ()
    #打印多少条记录
    count =  cursor.execute("SELECT  sum(executedImpression) FROM `dsp_daily_solution_winnotice` where time >  '%s'  and  solutionid = '%s'  "  % (date,id)  )
    #print count
    #打印具体内容
    info = cursor.fetchmany(count)
    for i in info:
        mysqlshow =  i[0]
        cursor.close ()  
        conn.close ()  
        return  mysqlshow

def main():
    day = datetime.datetime.today().strftime("%Y-%m-%d")
    date = datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")
    print day
    sid = get_solutionid(day)
    for id in sid:
        #print id
        show = 'show'
        mongorow = mongo_connection_show(day,id)
        mongoshow = mongo_show(mongorow,show)
        mysqlshow  = mysql_show(date,id)
        if mongoshow  < mysqlshow :
            print  id,'mongoshow:',mongoshow,'mysqlshow:',mysqlshow
     

if __name__ == '__main__':
    main()
