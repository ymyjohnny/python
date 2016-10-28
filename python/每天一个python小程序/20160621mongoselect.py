#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-6-21
@author: ymy
Copyright ymyjohnny@gmail.com
'''
import pymongo
import json
import time
import socket
import requests


#def mongo_connection_show(ip,db):
client=pymongo.MongoClient("221.228.228.4",27018)
db=client.unionfc0
conn=db.user_solution_impression
conn
        #id = long(int(id))
        #print id
print conn.find_one()
        #print count
        #conn.close()
        
