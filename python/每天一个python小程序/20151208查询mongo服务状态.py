#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-8
@author: ymy
Copyright ymyjohnny@gmail.com
'''
import pymongo


def mongo_getstat(ip,port):
    info =  pymongo.MongoClient( ip,port).server_info()
    for k,v in info.items():
        print k,':' ,v

    
def main():
     mongo_getstat('111.111.111.111',27017)


if __name__ == '__main__':
    main()
