#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年3月1日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo


def mongo_connection_show(oid,date):
    client=pymongo.MongoClient("221.228.90.4",27018)
    db=client.gdb
    conn=db.daily_sum
    conn
    #oid = 200014655
    #date = "2017-01-02"
    #return conn.find({"id": oid,"date": date}) 
    return conn.find({"id": oid}) 

def main():
    for i in  mongo_connection_show(200014655,"2017-01-02"):
        print i

if __name__ == '__main__':
    main()