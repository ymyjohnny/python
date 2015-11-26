#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-25
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import pymongo
#import subprocess
import os
import json

dict = {}

#serverinfo =  (subprocess.check_output(["facter"]))
serverinfo = os.popen("facter").read()
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

mongoclient = pymongo.MongoClient('111.111.111.111', 27018)
db = mongoclient.hostbase

db.info.save(dict)

#print dict
f = open('/data/hostbase','w')
json.dump(dict, f)
