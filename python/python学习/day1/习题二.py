#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''
import os

d_size ={}
for root,dirs,files in os.walk('/home/ymy/workspace/pytest/'):
   # print root
   for file in files:
      filename = os.path.join(root,file)
    #  print filename
      
      fsize = os.stat(filename).st_size
      #print fsize
      d_size.setdefault(fsize,[]).append(filename)
 #     d_size.append(fsize,filename)
#print d_size
#print d_size.items()

for k,v in d_size.items():
    if len([v]) <= 0:
        continue
    print v
    
    
import subprocess    
print subprocess.check_output(["ls","-l","/home/ymy"])

#print pid