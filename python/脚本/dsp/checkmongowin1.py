#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-15
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb,pymongo
import datetime



def mysql_connection_row(user,passwd,db,ip,port,sql):
    conn=MySQLdb.connect(host=ip,user=user,passwd=passwd,db=db)
    cursor = conn.cursor ()
    count =  cursor.execute(sql )
    info = cursor.fetchmany(count)
    for i in info:
        yield i
    cursor.close ()  
    conn.close ()  

def get_solutionid(row):
    for i in row:
        mysqlsid =  i[0]
        yield mysqlsid


def mongo_connection_show(day,id):
        client=pymongo.MongoClient('221.228.228.72',27018)
        db=client.sdb
        conn=db.daily_sum
        for i in  conn.find({"date":day,'id':id}):
            yield i

def mongo_show(row,keys):
    for item in row:
        return item[keys]
        
def mysql_show(date,id):
    conn=MySQLdb.connect(host="221.228.228.4",user="ymy",passwd="uqcqa8zd",db="dsp_test")
    cursor = conn.cursor ()
    count =  cursor.execute("SELECT  sum(executedImpression) FROM `dsp_daily_solution_winnotice` where time >  '%s'  and  solutionid = '%s'  "  % (date,id)  )
    info = cursor.fetchmany(count)
    for i in info:
        mysqlshow =  i[0]
        cursor.close ()  
        conn.close ()  
        return  mysqlshow

def main():
    day = datetime.datetime.today().strftime("%Y-%m-%d")
    date = datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")
    user = 'ymy'
    passwd = 'uqcqa8zd'
    db = 'dsp_test'
    ip = '221.228.228.4'
    port = '3306'
    getsolutionsql =  "SELECT * FROM `dsp_daily_solution_winnotice` where time >= '%s' group by solutionid "  % day
    sid = mysql_connection_row(user,passwd,db,ip,port,getsolutionsql)
    
    for id in sid:
        #print id
        show = 'show'
        mongorow = mongo_connection_show(day,id)
        try:
            mongoshow = mongo_show(mongorow,show)        
            mysqlshow  = mysql_show(date,id)
        except Exception:
            continue
            return Exception
        if mysqlshow < 100:
            continue
        if mongoshow   < mysqlshow :
            print  id,'mongoshow:',mongoshow,'mysqlshow:',mysqlshow
        
     

if __name__ == '__main__':
    main()

