#!/usr/bin/python
#coding=utf-8
'''
Created on 2017-6-28
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo
import MySQLdb
import datetime


def getmonitor(date,date1):
    l = []
    conn=MySQLdb.connect(host="192.168.32.4",user="root",passwd="uqcqa8zd",db="dsp")
    cursor = conn.cursor ()
    data = cursor.execute("SELECT  id  FROM  dsp_orders  WHERE  end_time <  '%s'  and   end_time >  '%s'" % (date,date1) )
    info = cursor.fetchmany(data)
    data1 = cursor.execute("SELECT group_id FROM dsp_orders WHERE  end_time > '%s' and group_id not in (SELECT group_id FROM  dsp_orders WHERE  end_time >  '%s' group by group_id) group by group_id" % (date1,date) )
    info1 = cursor.fetchmany(data1)
    for row in info:
        row = row[0]
        l.append(row)
    for row in info1:
        row = row[0]
        l.append(row)
    return l
    cursor.close ()
    conn.close ()

def mongo_del(ip,db,l):
        client=pymongo.MongoClient(ip,27018)
        db = str(db)
        db = "unionfc" + db
        print db
        db=client.get_database(db)
        conn=db.get_collection("user_solution_impression")
        #id = long(int(id))
        #print id
        for i in l:
            i = str(i)
            print i
            print conn.update( {  i: {"$exists":1}}, {"$unset": { i: 1}},multi = True, upsert = False  )


def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(days=30)
    d3 = d1 - datetime.timedelta(days=60)
    date = d2.strftime("%Y-%m-%d %H:%M:%S")
    date1 = d3.strftime("%Y-%m-%d %H:%M:%S")
    l = getmonitor(date,date1)
    for a in range(499,500):
        mongo_del('192.168.32.4',a ,l)

if __name__ == '__main__':
    main()