#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-6-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import pymongo
import json

def mongo_connection_show(ip,db):
        client=pymongo.MongoClient(ip,27018)
        db=client.get_database(db)
        #conn=db.get_collection("user_solution_impression")
        conn=db.get_collection("user_solution_impression")
        #id = long(int(id))
        #print id
        return conn

def main():
    for a in range(0,1):
         #print 1
         index = mongo_connection_show('221.228.228.4','unionfc%d' % a)
         for x in index:
           print x

       #print index


if __name__ == '__main__':
    main()