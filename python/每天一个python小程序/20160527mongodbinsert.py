#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import pymongo
#import subprocess
import os
import json

dict = {}

#serverinfo =  (subprocess.check_output(["facter"]))
serverinfo = os.popen("cat /data/ymy/testlog").read()
print serverinfo

for i in serverinfo.splitlines():
      if 'SSHFP' in i:
        continue
      if '/dev/' in i:
        continue
      if '/usr/local/java/' in i:
        continue
      if 'lsbrelease' in i:
        continue
      dict[str(i.split('=>')[0].strip())] = str(i.split('=>')[1].strip())
#print dict

mongoclient = pymongo.MongoClient('192.168.32.170', 27018)
db = mongoclient.unionfc8

db.user_solution_impression2.save(dict)

#print dict
f = open('/data/hostbase','w')
json.dump(dict, f)
