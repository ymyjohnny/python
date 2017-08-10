#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-30
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo


mongoclient = pymongo.MongoClient('192.168.32.46, 27018')
db = mongoclient.database_names()


print db