import os
from os import path
from os.path import join, getsize


d_size ={}
for root, dirs, files in os.walk('/tmp'):
    for file in files:
    #    if '-' not in file:
    #        continue
#        filenameall = os.path.join(dirs, file)
        filenameall = path.join(root,file)
        #print filenameall
        try:
             sizef = os.stat(filenameall)
        except:
            continue
        if sizef.st_size == 0:
            continue
        #print sizef.st_size
        d_size.setdefault(sizef.st_size, []).append(filenameall)
#print d_size
for k,v in d_size.items():
    if len(v) <= 1:
        continue       
    print v
        #print d_size
        


           
           
        

