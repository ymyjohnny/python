#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-30
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo


mongoclient = pymongo.MongoClient('221.228.231.151, 27018')
db = mongoclient.database_names()


print db