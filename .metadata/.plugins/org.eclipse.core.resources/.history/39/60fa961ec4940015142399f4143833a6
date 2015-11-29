#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo


mongoclient = pymongo.MongoClient('111.111.111.111', 27018)
db = mongoclient.hostbase

conn = db.info
keys = "host"


def get_mongo(conn):
    for row in conn.find():
        yield row

def print_base(row,keys):
    for item in row:
        #print item
        print "hostname: %s" % item[keys]

def main():
    row  = get_mongo(conn)
    print_base(row,keys)
    
if __name__ == '__main__':
    main()        


# for i in dict.splitlines():
#     print i